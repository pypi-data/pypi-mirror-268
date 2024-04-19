import re

import requests
from django.conf import settings
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from wagtail import hooks
from wagtail.images import get_image_model


@hooks.register("insert_editor_js")
def fileselector_js():
    return format_html(
        '<script src="https://mfstatic.com/js/fileselector.min.js"></script>'
    ) + mark_safe(
        """
            <script>            
                window.addEventListener('DOMContentLoaded', (event) => {
                    let prevChooseHandler = window.IMAGE_CHOOSER_MODAL_ONLOAD_HANDLERS.choose;                    
                    window.IMAGE_CHOOSER_MODAL_ONLOAD_HANDLERS.choose = (e,t) => {
                        window.MediaflowImageModal = e;                             
                        prevChooseHandler(e,t);                        
                    }                    
                });
            </script>
            """
    )


@hooks.register("after_publish_page")
def register_file_usage(request, page):    
    # Call the process_data method on the page
    for field in page.specific._meta.fields:
        name = str(field)        
        try:
            short_name = name[name.rindex(".") + 1 :]
        except:
            break
        if ("wagtailcore" not in name) and ("page_ptr" not in short_name):

            val = str(getattr(page.specific, short_name, None))            
            matches = re.findall(r"data-mf-image-id=\"([0-9]+)\"",val)            
            
            for id_image in matches:
                try:
                    report_usage(page, id_image)                   
                except:                    
                    pass

            matches = re.findall(r"<embed ([^>]+)>",val)
            for match in matches:
                if 'image' in match:
                    matches2 = re.findall(r"id=\"([0-9]+)\"",match)                    
                    model = get_image_model()

                    for id in matches2:
                        try:
                            image = model.objects.filter(id=id)[0]
                            meta_mapping = getattr(settings, "MEDIAFLOW_META_MAPPING", "")
                            for key in meta_mapping:
                                if key == "id":                
                                    id_image = getattr(image,meta_mapping[key])
                                    report_usage(page, id_image)
                                    break
                        except:
                            pass

                        
def report_usage(page, id_image):
    req = requests.get(
        "https://api.mediaflow.com/1/oauth2/token?client_id=" + getattr(settings, "MEDIAFLOW_CLIENT_ID", "") + 
        "&client_secret=" + getattr(settings, "MEDIAFLOW_CLIENT_SECRET", "") + "&grant_type=refresh_token&refresh_token=" + getattr(settings, "MEDIAFLOW_SERVER_KEY", ""),
        headers={"Accept": "application/json"},
    )
    token = req.json()["access_token"]
    web = {"page": page.full_url, "pageName": page.title}
    post_data = {
        "contact": str(page.owner),
        "types": ["web"],
        "web": web,
        "project": str(page.get_site()),
        "date": str(page.last_published_at),
    }
    req = requests.post(
        "https://api.mediaflow.com/1/file/"
        + str(id_image)
        + "/usage?access_token="
        + token,
        json=post_data,
        headers={"Accept": "application/json"},
    )
    
