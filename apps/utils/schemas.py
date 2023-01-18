import re

from drf_spectacular.openapi import AutoSchema


class SharedSwaggerSchema(AutoSchema):
    def get_tags(self):
        pattern = r"app_helpers\/(.*?)\/"
        tags = re.findall(pattern, self.path)
        return tags
