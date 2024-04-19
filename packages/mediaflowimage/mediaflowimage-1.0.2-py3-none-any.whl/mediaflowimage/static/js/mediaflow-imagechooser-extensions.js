// This is the js-file that is used by our custom FileInput widget import_button.html
// the widget is a django FileInput with an extra button to open
// 'Insert from Mediaflow' modal

$(document).ready(function () {
  const server_key = $('#mf-server-key').val();
  const client_id = $('#mf-client-id').val();
  const client_secret = $('#mf-client-secret').val();
  if (!window.MediaflowImageModal) {
    console.error('Mf Image Modal failed to initialize')
    return
  }

  let locale = $('#mf-locale').val()
  switch(locale) {
    case 'en':
      locale = 'en_US';
      break;
      case 'no':
      case 'nb':
      locale = 'nb_NO';
      break;
      case 'fi':
      locale = 'fi_FI';
      break;
      case 'sv':
      locale = 'sv_SE';
      break;
      case 'de':
      locale = 'de_DE';
      break;
      default:
      locale = 'en_US';
  }
  
  
  function getFileInfo(data, fileData) {
    const server_key = $('#mf-server-key').val();
    const client_id = $('#mf-client-id').val();
    const client_secret = $('#mf-client-secret').val();
    const mapping_jsonstr = $('#mf-meta-mapping').val().replaceAll("'",'"')

    const meta_mapping = JSON.parse(mapping_jsonstr)

    let fields = 'id,filename,name'

    for(key of Object.keys(meta_mapping)) {
      fields += "," + key
    }
    
    $.ajax({
      contentType: false,
      processData: false,
      type: 'GET',
      url: `https://api.mediaflow.com/1/oauth2/token?client_id=${client_id}&client_secret=${client_secret}&grant_type=refresh_token&refresh_token=${server_key}`
    }).done(function (tokenData) {      
      $.ajax({
        beforeSend: function (request) {
          request.setRequestHeader('Authorization', `Bearer ${tokenData.access_token}`)
        },
        contentType: false,
        processData: false,
        type: 'GET',
        url: `https://api.mediaflow.com/1/file/${data.id}?fields=${fields}&access_token=${tokenData.access_token}`
      }).done(function (metaData) {      
        if(metaData && metaData.length == 1) {
           uploadAndUse(new File([fileData], metaData[0].filename), metaData[0])
        } else {
          alert('A communication error occurred')
        }
        
      })
      
    })

  }

  function uploadAndUse(imageFile, metaData) {
    
    let formData = new FormData()
    let csrfToken = $('[name=csrfmiddlewaretoken]').val()
    let collectionId = 1
    let chooserParts = window.MediaflowImageModal.url.split('?')
    let createUrl = chooserParts[0] + 'create/'
    let idImage = 0
    if (chooserParts.length > 1) {
      createUrl += '?' + chooserParts[1]
    }

    if ($('#id_image-chooser-upload-collection').length) {
      collectionId = $('#id_image-chooser-upload-collection').val()
    }
    formData.append('image-chooser-upload-title', metaData.name)
    formData.append('image-chooser-upload-collection', collectionId)
    formData.append('image-chooser-upload-file', imageFile)
    formData.append('image-chooser-upload-tags', '')
    formData.append('image-chooser-upload-focal_point_x', '')
    formData.append('image-chooser-upload-focal_point_y', '')
    formData.append('image-chooser-upload-focal_point_width', '')
    formData.append('image-chooser-upload-focal_point_height', '')

    const mapping_jsonstr = $('#mf-meta-mapping').val().replaceAll("'",'"')
    const meta_mapping = JSON.parse(mapping_jsonstr)
    for(key of Object.keys(meta_mapping)) {
      if(key == "id") {
         idImage = metaData[key]
      }

      let fields = meta_mapping[key].split(',');
      for (let field of fields) {
        formData.append('image-chooser-upload-' + field, metaData[key] || '')  
      }

      
    }
    $.ajax({
      beforeSend: function (request) {
        request.setRequestHeader('X-CSRFToken', csrfToken)
      },
      contentType: false,
      data: formData,
      processData: false,
      type: 'POST',
      url: createUrl,
    }).done(function (data) {      
      /*
        if (idImage > 0) {
          reportUsage(idImage)
        }
        */
      
      $('#tab-label-upload')[0].click()      
      // This will 'magically' move the modalWorkflow along...
      window.MediaflowImageModal.loadResponseText(JSON.stringify(data))
      
    })
  }

  function reportUsage(idImage) {
    $.ajax({
      url: `https://api.mediaflow.com/1/oauth2/token?client_id=${client_id}&client_secret=${client_secret}&grant_type=refresh_token&refresh_token=${server_key}`,
      cache: false,
      success: function (data) {

        post_data = {    
          "contact": "Wagtail",
          "project": "Wagtail",
          "types": ["web"],
          "web": {"page": "Mediabank upload", "pageName": ""},
          "date": (new Date()).toISOString(),
          
      }
        $.ajax({
          url: `https://api.mediaflow.com/1/file/${idImage}/usage?access_token=${data.access_token}`,
          cache: false,
          contentType: 'application/json',
          method: 'POST',
          data: JSON.stringify(post_data),
          error: function (e) {
            console.error(e)
          },
        })
        
      },
      error: function (e) {
        console.error(e)
      },
    })
  }



  function startImport(data) {
    $.ajax({
      url: data.url,
      cache: false,
      xhr: function () {
        var xhr = new XMLHttpRequest()
        xhr.responseType = 'blob'
        return xhr
      },
      success: function (binaryData) {
        // TODO: How come we don't get the full filename with extension from fileselector?
        getFileInfo(data, binaryData)
        
      },
      error: function (e) {
        console.error(e)
      },
    })
  }

  // Inject our own tab + click behaviour (not so stylish approach but it works)
  let tabTitle = 'Insert from Mediaflow'
  switch(locale) {
    case 'sv_SE': tabTitle = 'Infoga från Mediaflow'
    break;
    case 'nb_NO': tabTitle = 'Sett inn fra Mediaflow'
    break;
    case 'de_DE': tabTitle = 'Aus Mediaflow einfügen'    
    break;
    case 'fi_FI': tabTitle = 'Lisää Mediaflowsta'
    break;
    
  }
  let tabLink = $(
      '<a id="tab-label-mfp-insert" href="#tab-mfp-insert" class="w-tabs__tab">'+ tabTitle + '</a>',
    ),
    newSection = $(
      '<section role="tabpanel" class="w-tabs__panel" id="tab-mfp-insert" hidden></section>',
    ),
    fileSelectorElement = $(
      '<div id="mf-fileselector" style="position:relative;min-height:460px" class="light"></div>',
    )

  newSection.append(fileSelectorElement)
  $('.modal-body .tab-content').append(newSection)
  $('.modal-body [role=tablist]').append(tabLink)

  tabLink.on('click', function (e) {
    e.preventDefault()
    $('.modal-body section').each(function () {
      if ($(this).attr('id') == 'tab-mfp-insert') {
        $(this).removeAttr('hidden')
      } else {
        $(this).attr('hidden', '')
      }
    })
    $('.modal-body .w-tabs a').each(function () {
      $(this).attr(
        'aria-selected',
        ($(this).attr('id') == 'tab-label-mfp-insert').toString(),
      )
    })
  })

  $('.modal-body a.w-tabs__tab').each(function () {
    if ($(this).attr('id') != 'tab-label-mfp-insert') {
      $(this).on('click', function () {
        $('#tab-mfp-insert').attr('hidden', '')
        $('#tab-label-mfp-insert').attr('aria-selected', 'false')
      })
    }
  })


  // Attach the fileselector to our own tab
  new FileSelector('mf-fileselector', {
    auth: 'token',
    // These are the same for all customers but should perhaps
    // be moved to app config / wagtail conf
    client_id: client_id,
    client_secret: client_secret,
    refresh_token: server_key,
    showDoneButton: false,
    limitFileType: 'jpg,png,webp,gif',
    viewLayout: 'thumbnails',
    allowCrop: true,
    noCropButton: false,
    showDoneButton: true,
    locale: locale,
    downloadFormat: 'mediaflow',
    success: function (responseData) {      
      startImport(responseData);
    },    
  })
})
