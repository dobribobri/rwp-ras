from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy
from django.utils import timezone


class IndexBlock(models.Model):
    h1 = models.CharField(verbose_name='Заголовок', null=True, blank=True, max_length=254)

    intro = models.TextField(verbose_name='Вводная часть', null=True, blank=True)

    h2_1 = models.CharField(verbose_name='Подзаголовок 1', null=True, blank=True, max_length=254)
    main_part_1 = models.TextField(verbose_name='Основная часть 1', null=True, blank=True)

    h2_2 = models.CharField(verbose_name='Подзаголовок 2', null=True, blank=True, max_length=254)
    main_part_2 = models.TextField(verbose_name='Основная часть 2', null=True, blank=True)

    coda = models.TextField(verbose_name='Заключительная часть', null=True, blank=True)

    def __str__(self):
        return "Главная - " + str(self.h1)

    class Meta:
        verbose_name = ugettext_lazy("Блок - Элемент главной страницы")
        verbose_name_plural = ugettext_lazy("Блоки - Элементы главной страницы")


class RightBlockMessage(models.Model):
    # order = models.IntegerField(verbose_name='Порядковый номер', primary_key=True)
    content = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return "Правая навигационная панель - {}".format(self.content)

    class Meta:
        verbose_name = ugettext_lazy("Блок - Сообщение правой навигационной панели")
        verbose_name_plural = ugettext_lazy("Блоки - Сообщения правой навигационной панели")


class SectionsBlock(models.Model):
    intro = models.TextField(verbose_name='Вводная часть', null=True, blank=True)

    h_1 = models.CharField(verbose_name='Заголовок 1', null=True, blank=True, max_length=254)
    desc_1 = models.TextField(verbose_name='Описание 1', null=True, blank=True)
    main_part_1 = models.TextField(verbose_name='Основная часть 1', null=True, blank=True)

    h_2 = models.CharField(verbose_name='Заголовок 2', null=True, blank=True, max_length=254)
    desc_2 = models.TextField(verbose_name='Описание 2', null=True, blank=True)
    main_part_2 = models.TextField(verbose_name='Основная часть 2', null=True, blank=True)

    coda = models.TextField(verbose_name='Заключительная часть', null=True, blank=True)

    def __str__(self):
        return "Блок \"Региональные отделения и секции\""

    class Meta:
        verbose_name = ugettext_lazy("Блок \"Региональные отделения и секции\"")
        verbose_name_plural = ugettext_lazy("Блок \"Региональные отделения и секции\"")


class BureauMember(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)

    image = models.ImageField(verbose_name='Фотография (3x4)', null=True, blank=True)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    def __str__(self):
        return "Члены Бюро - " + str(self.fio)

    class Meta:
        verbose_name = ugettext_lazy("Член Бюро")
        verbose_name_plural = ugettext_lazy("Члены Бюро")


class FileTypes:
    choices = (
        ('Файл PDF', 'Файл PDF'),
        ('Документ Word', 'Документ Word'),
        ('Документ Excel', 'Документ Excel'),
        ('Документ ODS', 'Документ ODS'),
        ('Изображение JPG/PNG/...', 'Изображение JPG/PNG/...'),
        ('ZIP-архив', 'ZIP-архив'),
        ('RAR-архив', 'RAR-архив'),
        ('', 'Другое')
    )


class ItemAchievement(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254,
                               default='Важнейшие научные достижения по проблеме Распространение радиоволн, ' +
                                       'полученные в 20xx и рекомендуемые в годичный отчет РАН')
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "Отчеты (достижения/результаты) - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Файл - Отчет (достижения/результаты)")
        verbose_name_plural = ugettext_lazy("Файлы - Отчеты о достижениях/результатах")


class ItemReport(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254,
                               default='Отчет о работе Научного Совета РАН по комплексной проблеме Распространение радиоволн за 20xx год')
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "Отчеты о работе - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Файл - Отчет о работе")
        verbose_name_plural = ugettext_lazy("Файлы - Отчеты о работе")


class ItemPlan(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254,
                               default='План работы Научного Совета на 20хх г.')
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "План работы - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Файл - План работы")
        verbose_name_plural = ugettext_lazy("Файлы - План работы")


class ItemSuggestions(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254,
                               default='Предложения Научного Совета о проведении конференций в 20xx-20xx гг.')
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "Предложения - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Файл - Предложения о мероприятиях")
        verbose_name_plural = ugettext_lazy("Файлы - Предложения о мероприятиях")


class ItemProtocol(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254,
                               default='Протокол заседания Бюро Научного Совета от xx.xx.20xx')
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "Протоколы - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Файл - Протокол заседания Бюро")
        verbose_name_plural = ugettext_lazy("Файлы - Протоколы заседаний Бюро")


class ItemParticipation(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254,
                               default='Сведения об участии 20xx-20xx гг.')
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "Сведения - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Файл - Сведения об участии в мероприятиях")
        verbose_name_plural = ugettext_lazy("Файлы - Сведения об участии в мероприятиях")


class ItemOther(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254)
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "Другое - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Файл - Другие документы")
        verbose_name_plural = ugettext_lazy("Файлы - Другие документы")


class ItemDecision(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254)
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "[Выключено] Решения - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("[Выключено] Файл - Решение Совета")
        verbose_name_plural = ugettext_lazy("[Выключено] Файлы - Решения Совета")


class ItemNDocs(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254)
    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return "[Выключено] Нормативные документы - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("[Выключено] Файл - Нормативная информация")
        verbose_name_plural = ugettext_lazy("[Выключено] Файлы - Нормативная информация")


class AnnouncementBlock(models.Model):
    caption = models.CharField(verbose_name='Заголовок', max_length=254)

    when = models.CharField(verbose_name='Когда', max_length=254)
    where = models.CharField(verbose_name='Где', max_length=254)

    desc = models.TextField(verbose_name='Описание / повестка дня', null=True, blank=True)

    def __str__(self):
        return "Анонс (заседания) - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Блок - Анонс (заседания)")
        verbose_name_plural = ugettext_lazy("Блоки - Анонсы (заседаний)")


class ConferenceBlock(models.Model):
    caption = models.CharField(verbose_name='Название конференции', max_length=254)

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    when = models.CharField(verbose_name='Когда', max_length=254)
    where = models.CharField(verbose_name='Где', max_length=254)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    def __str__(self):
        return "Конференция - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Блок - Конференция")
        verbose_name_plural = ugettext_lazy("Блоки - Конференции")


class SeminarBlock(models.Model):
    caption = models.CharField(verbose_name='Название семинара', max_length=254)

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    when = models.CharField(verbose_name='Когда', max_length=254)
    where = models.CharField(verbose_name='Где', max_length=254)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    def __str__(self):
        return "Семинар - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Блок - Семинар")
        verbose_name_plural = ugettext_lazy("Блоки - Семинары")


class ProjectBlock(models.Model):
    caption = models.CharField(verbose_name='Название проекта', max_length=254)

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    desc = models.TextField(verbose_name='Информация')

    def __str__(self):
        return "Проект - " + str(self.caption)

    class Meta:
        verbose_name = ugettext_lazy("Блок - Проект (Совместный проект)")
        verbose_name_plural = ugettext_lazy("Блоки - Проекты (Совместные проекты)")


class ContactsBlock(models.Model):
    content = models.TextField(verbose_name='Содержание', null=True, blank=True)

    def __str__(self):
        return "Блок \"Контакты\""

    class Meta:
        verbose_name = ugettext_lazy("Блок \"Контакты\"")
        verbose_name_plural = ugettext_lazy("Блок \"Контакты\"")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    sex_choices = (
        ('м', 'муж.'),
        ('ж', 'жен.'),
    )
    sex = models.CharField(verbose_name='Пол', max_length=4, choices=sex_choices, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=100, null=True, blank=True)
    education = models.CharField(verbose_name='Образование', max_length=100, null=True, blank=True)
    degree = models.CharField(verbose_name='Ученая степень', max_length=100, null=True, blank=True)
    title = models.CharField(verbose_name='Ученое звание', max_length=100, null=True, blank=True)

    filled = models.BooleanField(verbose_name='Заполнены основные поля', default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = ugettext_lazy("Профиль пользователя")
        verbose_name_plural = ugettext_lazy("Профили пользователей")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
