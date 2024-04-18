#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm
__all__ = [
    'User',
    'Group',
    'GroupUserRel'
]
import unicodedata

from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# Create your models here.
from django.utils.crypto import salted_hmac
from django.utils.translation import gettext_lazy as _

from rest_framework_admin.user.configs import MemberRoleEnum
from rest_framework_util.db.models.base import BaseModel, BaseRelModel
from rest_framework_util.db.models.manager import UserModelManager


class User(BaseModel):
    username = models.CharField(
        '用户名',
        max_length=32,
        help_text=_(
            'Required. 32 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        unique=True,
    )
    password = models.CharField('密码', max_length=128)
    nickname = models.CharField('昵称', max_length=64, blank=True, null=True)
    email = models.EmailField('邮箱')
    last_login = models.DateTimeField('最后登录时间', blank=True, null=True)
    phone = models.CharField('电话', max_length=64, blank=True, null=True)
    avatar = models.CharField('头像', max_length=256, null=True, blank=True)
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.RESTRICT,
        related_name="created_%(app_label)s_%(class)ss",
        blank=True, null=True
    )
    role = models.CharField(
        max_length=32,
        choices=[(_.name, _.value) for _ in MemberRoleEnum],
        null=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserModelManager()

    # Stores the raw password if set_password() is called so that it can
    # be passed to password_changed() after the model is saved.
    _password = None

    class Meta:
        verbose_name = _('user')
        db_table = 'user'

    def get_username(self):
        """Return the username for this User."""
        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):
        return f'User(id={self.id}, username={self.get_username()})'

    def clean(self):
        setattr(
            self,
            self.USERNAME_FIELD,
            self.normalize_username(
                self.get_username()))
        self.email = self.__class__.objects.normalize_email(self.email)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    @classmethod
    def normalize_username(cls, username):
        return unicodedata.normalize('NFKC', username) if isinstance(
            username, str) else username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    def _legacy_get_session_auth_hash(self):
        # RemovedInDjango40Warning: pre-Django 3.1 hashes will be invalid.
        # key_salt = 'django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash'
        key_salt = 'rest_framework_admin.user.models.User.get_session_auth_hash'
        return salted_hmac(key_salt, self.password,
                           algorithm='sha1').hexdigest()

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        # key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        key_salt = 'rest_framework_admin.user.models.User.get_session_auth_hash'
        return salted_hmac(
            key_salt,
            self.password,
            # RemovedInDjango40Warning: when the deprecation ends, replace
            # with:
            # algorithm='sha256',
            algorithm=settings.DEFAULT_HASHING_ALGORITHM,
        ).hexdigest()

    @property
    def name(self):
        """ 为了与BaseModel字段匹配 """
        return self.nickname

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    @property
    def is_staff(self):
        return self.role in MemberRoleEnum._member_names_

    @property
    def is_admin_or_owner(self):
        """ 管理员或者创建者 """
        return MemberRoleEnum.is_admin_or_owner(self.role)

    @property
    def current_tenant(self):
        if hasattr(self, '_current_tenant'):
            return self._current_tenant
        from rest_framework_admin.tenant.models import TenantUserRel
        rel_query = TenantUserRel.objects.filter(user_id=self.id)
        if rel_query.filter(is_current=True).first():
            rel = rel_query.filter(is_current=True).first()
        else:
            rel = rel_query.first()
        self.current_tenant_id = rel.tenant_id if rel else None
        return self._current_tenant

    @current_tenant.setter
    def current_tenant(self, value):
        from rest_framework_admin.tenant.models import TenantUserRel
        tenant = value
        rel = TenantUserRel.objects.filter(
            tenant_id=tenant.id, user_id=self.id).first()
        if rel:
            tenant.current_role = rel.role
        else:
            tenant = None
        self._current_tenant = tenant

    @property
    def current_tenant_id(self):
        return self._current_tenant.id

    @current_tenant_id.setter
    def current_tenant_id(self, value):
        try:
            from rest_framework_admin.tenant.models import TenantUserRel
            rel = TenantUserRel.objects.filter(
                tenant_id=value, user_id=self.id).first()
            if rel:
                tenant = rel.tenant
                tenant.current_role = rel.role
            else:
                tenant = None
        except BaseException:
            tenant = None

        self._current_tenant = tenant


class BaseUserRel(BaseRelModel):
    user = models.ForeignKey(User, models.CASCADE)
    role = models.CharField(
        max_length=32,
        choices=[(_.name, _.value) for _ in MemberRoleEnum])

    class Meta:
        abstract = True


from rest_framework_admin.user.group.models import Group, GroupUserRel
