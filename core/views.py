from rest_framework import mixins, viewsets


class CreateRetrieveUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `create`, and `update` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    http_method_names = ["get", "post", "put"]


class ListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    A viewset that provides `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    http_method_names = ["get", "post", "put"]
