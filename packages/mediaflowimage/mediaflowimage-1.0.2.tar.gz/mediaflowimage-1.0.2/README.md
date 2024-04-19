
# Mediaflow image plugin for Wagtail


## Installation
      pip install mediaflowimage

### Edit your site settings file

- Add **"mediaflowimage"** to the array **INSTALLED_APPS** 

- Tell Wagtail to use a custom image form

      WAGTAILIMAGES_IMAGE_FORM_BASE = 'mediaflowimage.forms.MediaflowImageForm'

- Add the API keys for the plugin (consult Mediaflow Support to get API keys)
  
      MEDIAFLOW_CLIENT_ID = <YOUR SERVER ID>
      MEDIAFLOW_CLIENT_SECRET = <YOUR CLIENT SECRET>
      MEDIAFLOW_SERVER_KEY = <YOUR SERVER KEY>

  
## Using the plugin

The plugin adds a new tab to the Image Creation Form. This works for inserting images in the Draftail editor as well as from an ImageChooserBlock. 
The tab lists all Mediaflow files that are shared to the integration. To insert an image, simply select it from the file selector. This will download the image from Mediaflow and store it to your configured Media location.

  
## Custom Image models
The image plugin works out of the box with the default wagtail image model, but if you want to map Mediaflow image metadata properties to wagtail images you need to use a custom image model. A custom image model is also required if you want to log image file usages in Mediaflow.

The fields of your image model can be mapped so that they are automatically populated when you insert (upload) an image from mediaflow. This is done by defining a mapping in your settings file like this:

    MEDIAFLOW_META_MAPPING  = {   
	    "photographer": "mf_photographer",    
	    "description": "mf_description",    
	    "id" : "mf_mediaflow_id"
    }
The keys of the object in this example refer to the Mediaflow fields and each corresponding value refers to a field name in your image model.  In the example above, the Mediaflow field **photographer** is mapped the the field **mf_photographer** of your image model.

If you need image usage reporting, the **MEDIAFLOW_META_MAPPING** must have a key **id**   that is mapped to a field in your image model ("mf_mediaflow_id" in the example) . Furthermore, your image model must have a custom rendition model that adds the **data-mf-image-id** attribute on all rendered images. 

An example custom image class that has a Mediaflow Id field and a custom rendition  is provided below. The image model field names correspond to the field names given in the setting **MEDIAFLOW_META_MAPPING** above:

    from django.conf import settings
    from django.db import models
    from django.utils.functional import cached_property
    from wagtail.images.models import AbstractImage, AbstractRendition, Image  
    
    class MyImage(AbstractImage):
        # Add any extra fields to image here    
        # To add a caption field:
        photographer = models.CharField(max_length=255, blank=True)
        description = models.CharField(max_length=255, blank=True)
        mediaflow_id = models.IntegerField(blank=True, default=0)
        admin_form_fields = Image.admin_form_fields + (
            # Then add the field names here to make them appear in the form:
            "description",
            "photographer",
            "mediaflow_id",
        )
            
    class CustomRendition(AbstractRendition):
        image = models.ForeignKey(
            MyImage, on_delete=models.CASCADE, related_name="renditions"
        )
    
        @cached_property
        def getIdField(self):
            meta_mapping = getattr(settings, "MEDIAFLOW_META_MAPPING", "")
            for key in meta_mapping:
                if key == "id":                
                    return getattr(self.image, meta_mapping[key])
            return 0
        
        
        @property
        def attrs_dict(self):
            attrs = super().attrs_dict
            idField = self.getIdField
            
            if idField > 0:
                attrs["data-mf-image-id"] = idField        
            return attrs
    
        class Meta:
            unique_together = (("image", "filter_spec", "focal_point_key"),)

## Useful references
* https://www.notion.so/mediaflowcom/Technical-Integration-Guide-22c2d7a206304071840d89666ec42e0c
* https://www.notion.so/mediaflowcom/Standard-API-Integration-for-CMS-and-other-platforms-obs-flyttat-till-k-b-8e57fe80c1e04fd99362c3a799ef036
