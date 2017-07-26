from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from filebrowser.fields import FileBrowseField

from blog.models import Article
from event.models import Event

# from team.models import Project

social_network = (
    ('mdi-github-circle', 'GitHub'),
    ('mdi-twitter', 'Twitter'),
    ('mdi-gmail', 'Mail'),
    ('mdi-vk', 'VK'),  # mdi-vk - ставится как иконка соц сети, а vk - видет пользователь
    ('mdi-facebook', 'Facebook'),
)

type_partner = (
    ('info', 'Информационный'),
    ('finance', 'Финансовый'),
    ('general', 'Генеральный'),
)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название социальной сети", choices=social_network)
    link = models.CharField(max_length=300, verbose_name="Ссылка на профиль")
    user = models.ForeignKey('Member')

    def __str__(self):
        return Member.get_full_name(self.user)

    class Meta:
        verbose_name = "социальных сетей"
        verbose_name_plural = "социальных сетей"


class TeamManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password, )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    email = models.EmailField(unique=True)
    git_username = models.CharField(max_length=300, verbose_name="Git username")
    groups = models.ManyToManyField(
        Group,
        verbose_name='Группа',
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )
    first_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Фамилия")

    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_image = FileBrowseField("Изображения профиля", max_length=200, directory="состав_клуба/", blank=True,
                                    null=True)

    """ Поля для вывода на странице "Команда" """
    description = models.TextField(max_length=300, null=False, blank=True, default='', verbose_name="Описание",
                                   help_text='Выводится в описании на странице "участники".')
    contact_link = models.CharField(max_length=300, null=False, blank=True, default='', verbose_name="Ссылка для связи",
                                    help_text='Выводится на странице "участники".')
    """ """

    objects = TeamManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = "Участника"
        verbose_name_plural = "Участники"

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.email

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.email

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Project(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    description = RichTextUploadingField(verbose_name="Описание")
    # Добавил слоган для проекта
    slug = models.SlugField(default='')
    sub_name = models.CharField(max_length=300, verbose_name="Слоган", null=True, blank=True)
    card_name = models.CharField(max_length=300, verbose_name="Название в списке", default='')
    members = models.ManyToManyField(Member, verbose_name="Участники проекта")
    git = models.URLField(verbose_name="Cсылка на Git", null=True, blank=True)
    image = FileBrowseField("Главное изображение", max_length=200, directory="images/", blank=True, null=True)

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Partner(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название партнера")
    slug = models.SlugField()
    type_partner = models.CharField(max_length=300, verbose_name="Тип партнера", choices=type_partner)
    description = RichTextUploadingField(verbose_name="Описание")
    site = models.CharField(verbose_name="Сайт", max_length=500)
    address = models.CharField(verbose_name="Адрес", max_length=500, blank=True, null=True)
    phone = models.CharField(verbose_name="Телефон", max_length=500, blank=True, null=True)
    image = FileBrowseField("Изображение", max_length=200, directory="images/", blank=True, null=True)

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class SEO(models.Model):
    seo_description = models.TextField(verbose_name="SEO Описание")
    key_words = models.TextField(verbose_name="Ключ слова")
    article = models.OneToOneField(Article, related_name='articles', null=True, blank=True)
    event = models.OneToOneField(Event, related_name="events", null=True, blank=True)
    project = models.OneToOneField(Project, related_name="projects", null=True, blank=True)

    def __str__(self):
        if self.article:
            return "SEO для статьи " + self.article.title
        elif self.event:
            return "SEO для мероприятия" + self.event.title
        else:
            return "SEO для проекта" + self.project.name

    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "SEO"
