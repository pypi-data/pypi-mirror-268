from django.conf import settings
from django.forms import FileInput
from django.utils import translation


# This widget is used by the Image Form 'MediaflowImageForm'
class MedialowFileInput(FileInput):
    template_name = "widgets/mediaflow-custom-imageinput.html"

    def get_context(self, name, value, attrs):
        locale = translation.get_language()
        if len(locale) < 1:
            locale = 'en'
        context = super(FileInput, self).get_context(name, value, attrs)
        mapping = getattr(settings, "MEDIAFLOW_META_MAPPING", "")
        context.update({"server_key": getattr(settings, "MEDIAFLOW_SERVER_KEY", "")})
        context.update({"client_id": getattr(settings, "MEDIAFLOW_CLIENT_ID", "")})
        context.update({"locale": locale})
        context.update(
            {"client_secret": getattr(settings, "MEDIAFLOW_CLIENT_SECRET", "")}
        )
        context.update({"meta_mapping": mapping})
        return context

    class Media:
        js = ["js/mediaflow-imagechooser-extensions.js"]
