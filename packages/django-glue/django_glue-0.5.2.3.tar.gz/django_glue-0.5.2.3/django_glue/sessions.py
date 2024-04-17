from time import time

from django.contrib.contenttypes.models import ContentType

from django_glue.conf import settings
from django_glue.enums import GlueConnection, GlueAccess
from django_glue.data_classes import GlueContextData, GlueMetaData
from django_glue.utils import generate_field_dict, generate_method_list, encode_query_set_to_str

GLUE_SESSION_TYPES = (
    'context',
    'meta',
)


class GlueSession:
    """
        Used to add models, query sets, and other objects to the session.
        Todo: What is context?
    """
    def __init__(self, request):
        self.request = request

        self.request.session.setdefault(settings.DJANGO_GLUE_SESSION_NAME, dict())

        for session_type in GLUE_SESSION_TYPES:
            self.request.session[settings.DJANGO_GLUE_SESSION_NAME].setdefault(session_type, dict())

        self.session = self.request.session[settings.DJANGO_GLUE_SESSION_NAME]

    def __getitem__(self, key):
        return self.session[key]

    def __setitem__(self, key, value):
        self.session[key] = value

    def add_function(
            self,
            unique_name: str,
            target,
    ):
        self.check_unique_name(unique_name)

        self.add_context(unique_name, GlueContextData(
            connection=GlueConnection('function'),
            access=GlueAccess('view'),
        ))

        self.add_meta(unique_name, GlueMetaData(
            function=target,
        ))

        self.set_modified()

    def add_model_object(
            self,
            unique_name: str,
            model_object,
            access: str = 'view',
            fields: tuple = ('__all__',),
            exclude: tuple = ('__none__',),
            methods: tuple = ('__none__',),
    ):
        content_type = ContentType.objects.get_for_model(model_object)

        self.check_unique_name(unique_name)

        self.add_context(unique_name, GlueContextData(
            connection=GlueConnection('model_object'),
            access=GlueAccess(access),
            fields=generate_field_dict(model_object, fields, exclude),
            methods=generate_method_list(model_object, methods),
        ))

        self.add_meta(unique_name, GlueMetaData(
            app_label=content_type.app_label,
            model=content_type.model,
            object_pk=model_object.pk,
            fields=fields,
            exclude=exclude,
            methods=methods,
        ))

        self.set_modified()

    def add_query_set(
            self,
            unique_name: str,
            query_set,
            access: str = 'view',
            fields: tuple = ('__all__',),
            exclude: tuple = ('__none__',),
            methods: tuple = ('__none__',),
    ):
        content_type = ContentType.objects.get_for_model(query_set.query.model)

        self.check_unique_name(unique_name)

        self.add_context(unique_name, GlueContextData(
            connection=GlueConnection('query_set'),
            access=GlueAccess(access),
            fields=generate_field_dict(query_set.query.model(), fields, exclude),
            methods=generate_method_list(query_set.query.model(), methods),
        ))

        self.add_meta(unique_name, GlueMetaData(
            app_label=content_type.app_label,
            model=content_type.model,
            query_set_str=encode_query_set_to_str(query_set),
            fields=fields,
            exclude=exclude,
            methods=methods,
        ))

        self.set_modified()

    def add_context(self, unique_name, context_data: GlueContextData) -> None:
        self.session['context'][unique_name] = context_data.to_dict()

    def add_template(
            self,
            unique_name: str,
            template,
    ):

        self.check_unique_name(unique_name)

        self.add_context(unique_name, GlueContextData(
            connection=GlueConnection('template'),
            access=GlueAccess('view'),
        ))

        self.add_meta(unique_name, GlueMetaData(
            template=template,
        ))

        self.set_modified()

    def add_meta(self, unique_name, meta_data: GlueMetaData) -> None:
        self.session['meta'][unique_name] = meta_data.to_dict()

    def check_unique_name(self, unique_name):
        if self.unique_name_unused(unique_name):
            self.purge_unique_name(unique_name)

    def clean(self, removable_unique_names):
        for unique_name in removable_unique_names:
            self.purge_unique_name(unique_name)

        self.set_modified()

    def has_unique_name(self, unique_name):
        return unique_name in self.session['context']

    def purge_unique_name(self, unique_name):
        for session_type in GLUE_SESSION_TYPES:
            if unique_name in self.session[session_type]:
                self.session[session_type].pop(unique_name)

    def set_modified(self):
        self.request.session.modified = True

    def unique_name_unused(self, unique_name):
        return unique_name in self.session['context']



class GlueKeepLiveSession:
    """
        Used to keep glue session data live for a set amount of time.
        Functionality to handle multiple windows/tabs.
    """
    def __init__(self, request):
        self.request = request
        self.session = request.session.setdefault(settings.DJANGO_GLUE_KEEP_LIVE_SESSION_NAME, dict())

    def __getitem__(self, key):
        return self.session[key]

    def __setitem__(self, key, value):
        self.session[key] = value

    def clean_and_get_expired_unique_names(self) -> list:
        expired_unique_names = []

        for key, val in self.session.items():
            if time() > val:
                expired_unique_names.append(key)

        for expired_unique_name in expired_unique_names:
            self.session.pop(expired_unique_name)

        self.set_modified()

        return expired_unique_names

    @staticmethod
    def get_next_expire_time():
        return time() + settings.DJANGO_GLUE_KEEP_LIVE_EXPIRE_TIME_SECONDS

    def set_unique_name(self, unique_name):
        self.session.setdefault(unique_name, self.get_next_expire_time())

        self.set_modified()

    def set_modified(self):
        self.request.session.modified = True

    def update_unique_names(self, unique_names: list):
        for unique_name in unique_names:
            if unique_name in self.session:
                self.session[unique_name] = self.get_next_expire_time()

        self.set_modified()
