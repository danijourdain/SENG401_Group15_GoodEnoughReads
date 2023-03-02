# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Author(models.Model):
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a_id = models.AutoField(db_column='A_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'author'


class Awards(models.Model):
    level = models.IntegerField(db_column='Level', primary_key=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255, blank=True, null=True)  # Field name made lowercase.
    required_xp = models.IntegerField(db_column='Required_XP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'awards'


class Book(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=255)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pages = models.IntegerField(db_column='Pages')  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Bookcase(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.ForeignKey('User', models.DO_NOTHING, db_column='Email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookcase'


class Bookinusercollection(models.Model):
    userrating = models.IntegerField(db_column='UserRating', blank=True, null=True)  # Field name made lowercase.
    newestreadingstartdate = models.DateField(db_column='NewestReadingStartDate', blank=True, null=True)  # Field name made lowercase.
    newestreadingenddate = models.DateField(db_column='NewestReadingEndDate', blank=True, null=True)  # Field name made lowercase.
    numberoftimesreread = models.PositiveIntegerField(db_column='NumberOfTimesReread', blank=True, null=True)  # Field name made lowercase.
    pagesread = models.PositiveIntegerField(db_column='PagesRead', blank=True, null=True)  # Field name made lowercase.
    isbn = models.OneToOneField(Book, models.DO_NOTHING, db_column='ISBN', primary_key=True)  # Field name made lowercase.
    email = models.ForeignKey('User', models.DO_NOTHING, db_column='Email')  # Field name made lowercase.
    shelfname = models.ForeignKey('Collection', models.DO_NOTHING, db_column='ShelfName', to_field='ShelfName')  # Field name made lowercase.
    collectionid = models.ForeignKey('Collection', models.DO_NOTHING, db_column='CollectionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookinusercollection'
        unique_together = (('isbn', 'shelfname', 'email'),)


class Collection(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, db_collation='utf8mb4_bin', blank=True, null=True)  # Field name made lowercase.
    statsid = models.ForeignKey('Statistics', models.DO_NOTHING, db_column='StatsID')  # Field name made lowercase.
    email = models.ForeignKey('Shelf', models.DO_NOTHING, db_column='Email', to_field='Email', blank=True, null=True)  # Field name made lowercase.
    shelfname = models.ForeignKey('Shelf', models.DO_NOTHING, db_column='ShelfName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collection'
        unique_together = (('id', 'shelfname'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Isapartof(models.Model):
    position = models.CharField(db_column='Position', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookisbn = models.OneToOneField(Book, models.DO_NOTHING, db_column='BookISBN', primary_key=True)  # Field name made lowercase.
    shelfname = models.ForeignKey('Shelf', models.DO_NOTHING, db_column='ShelfName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'isapartof'
        unique_together = (('bookisbn', 'shelfname'),)


class Shelf(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=255, db_collation='utf8mb4_bin')  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=255, db_collation='utf8mb4_bin', blank=True, null=True)  # Field name made lowercase.
    visibility = models.CharField(db_column='Visibility', max_length=255, db_collation='utf8mb4_bin', blank=True, null=True)  # Field name made lowercase.
    pinnedshelfposition = models.PositiveIntegerField(db_column='PinnedShelfPosition', blank=True, null=True)  # Field name made lowercase.
    email = models.ForeignKey('User', models.DO_NOTHING, db_column='Email')  # Field name made lowercase.
    bookcaseid = models.ForeignKey(Bookcase, models.DO_NOTHING, db_column='BookCaseID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shelf'
        unique_together = (('name', 'email', 'bookcaseid'),)


class Statistics(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.ForeignKey('User', models.DO_NOTHING, db_column='Email')  # Field name made lowercase.
    totalpagesread = models.PositiveIntegerField(db_column='TotalPagesRead', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statistics'
        unique_together = (('id', 'email'),)


class User(models.Model):
    email = models.CharField(db_column='Email', primary_key=True, max_length=255, db_collation='utf8mb4_bin')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profilepictureurl = models.CharField(db_column='ProfilePictureURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    xp = models.IntegerField(db_column='XP')  # Field name made lowercase.
    awardprofile = models.ForeignKey(Awards, models.DO_NOTHING, db_column='AwardProfile')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Writtenby(models.Model):
    bookisbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookISBN')  # Field name made lowercase.
    authorid = models.OneToOneField(Author, models.DO_NOTHING, db_column='AuthorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'writtenby'
        unique_together = (('authorid', 'bookisbn'),)
