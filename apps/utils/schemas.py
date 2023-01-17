import re

from drf_spectacular.openapi import AutoSchema


class SharedSwaggerSchema(AutoSchema):
    def get_tags(self):
        pattern = r"shared\/(.*?)\/"
        tags = re.findall(pattern, self.path)
        return tags
