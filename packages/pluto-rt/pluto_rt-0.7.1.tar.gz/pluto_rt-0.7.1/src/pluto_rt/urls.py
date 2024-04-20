from django.urls import converters, path, register_converter
from pluto_rt import views


class PlutoRTPath(converters.PathConverter):
    """Path with "pluto_rt" only, to prevent leaking sensitive information."""

    def to_python(self, value):
        if "pluto_rt" not in value:
            raise ValueError("Invalid path")
        return super().to_python(value)


register_converter(PlutoRTPath, "pluto_rt_path")

app_name = "pluto_rt"
urlpatterns = [
    # Private API view returns and pops items from named queue
    path("sse/<str:queue_name>/<pluto_rt_path:item_template>", view=views.rt_sse, name="sse"),
    path(
        "polling/<str:queue_name>/<pluto_rt_path:item_template>",
        view=views.rt_polling,
        name="polling",
    ),
]
