BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "accounts_customuser_groups" (
	"id"	integer NOT NULL,
	"customuser_id"	bigint NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("customuser_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "accounts_customuser_user_permissions" (
	"id"	integer NOT NULL,
	"customuser_id"	bigint NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("customuser_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	bigint NOT NULL,
	"action_time"	datetime NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "chat_article" (
	"id"	integer NOT NULL,
	"title"	varchar(200) NOT NULL,
	"body"	text NOT NULL,
	"image"	varchar(100),
	"created_at"	datetime NOT NULL,
	"author_id"	bigint NOT NULL,
	FOREIGN KEY("author_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "chat_article_likes" (
	"id"	integer NOT NULL,
	"article_id"	bigint NOT NULL,
	"customuser_id"	bigint NOT NULL,
	FOREIGN KEY("customuser_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("article_id") REFERENCES "chat_article"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "chat_comment" (
	"id"	integer NOT NULL,
	"title"	varchar(100),
	"body"	text NOT NULL,
	"created_at"	datetime NOT NULL,
	"article_id"	bigint NOT NULL,
	"author_id"	bigint NOT NULL,
	"parent_id"	bigint,
	FOREIGN KEY("author_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("article_id") REFERENCES "chat_article"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("parent_id") REFERENCES "chat_comment"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "chat_notification" (
	"id"	integer NOT NULL,
	"message"	text NOT NULL,
	"is_read"	bool NOT NULL,
	"timestamp"	datetime NOT NULL,
	"recipient_id"	bigint NOT NULL,
	FOREIGN KEY("recipient_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "chat_privatemessage" (
	"id"	integer NOT NULL,
	"body"	text NOT NULL,
	"timestamp"	datetime NOT NULL,
	"is_read"	bool NOT NULL,
	"recipient_id"	bigint NOT NULL,
	"sender_id"	bigint NOT NULL,
	FOREIGN KEY("sender_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("recipient_id") REFERENCES "accounts_customuser"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "accounts_customuser" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"first_name"	varchar(30) NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_name"	varchar(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2024-07-16 21:41:35.562945');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (2,'contenttypes','0002_remove_content_type_name','2024-07-16 21:41:35.583426');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (3,'auth','0001_initial','2024-07-16 21:41:35.612867');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (4,'auth','0002_alter_permission_name_max_length','2024-07-16 21:41:35.633115');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (5,'auth','0003_alter_user_email_max_length','2024-07-16 21:41:35.662869');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (6,'auth','0004_alter_user_username_opts','2024-07-16 21:41:35.683712');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (7,'auth','0005_alter_user_last_login_null','2024-07-16 21:41:35.692837');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (8,'auth','0006_require_contenttypes_0002','2024-07-16 21:41:35.704031');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (9,'auth','0007_alter_validators_add_error_messages','2024-07-16 21:41:35.719820');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (10,'auth','0008_alter_user_username_max_length','2024-07-16 21:41:35.732649');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (11,'auth','0009_alter_user_last_name_max_length','2024-07-16 21:41:35.742720');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (12,'auth','0010_alter_group_name_max_length','2024-07-16 21:41:35.762710');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (13,'auth','0011_update_proxy_permissions','2024-07-16 21:41:35.777806');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (14,'auth','0012_alter_user_first_name_max_length','2024-07-16 21:41:35.793090');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (15,'accounts','0001_initial','2024-07-16 21:41:35.821811');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (16,'admin','0001_initial','2024-07-16 21:41:35.850998');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (17,'admin','0002_logentry_remove_auto_add','2024-07-16 21:41:35.879681');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (18,'admin','0003_logentry_add_action_flag_choices','2024-07-16 21:41:35.895338');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (19,'sessions','0001_initial','2024-07-16 21:41:35.912756');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (20,'chat','0001_initial','2024-07-16 21:48:44.502855');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (21,'accounts','0002_alter_customuser_options_alter_customuser_managers_and_more','2024-07-16 22:30:42.901866');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (2,'auth','permission');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (3,'auth','group');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (4,'contenttypes','contenttype');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (5,'sessions','session');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (6,'accounts','customuser');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (7,'chat','comment');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (8,'chat','notification');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (9,'chat','article');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (10,'chat','privatemessage');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (13,4,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (14,4,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (15,4,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (16,4,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (17,5,'add_session','Can add session');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (18,5,'change_session','Can change session');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (19,5,'delete_session','Can delete session');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (20,5,'view_session','Can view session');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (21,6,'add_customuser','Can add user');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (22,6,'change_customuser','Can change user');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (23,6,'delete_customuser','Can delete user');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (24,6,'view_customuser','Can view user');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (25,7,'add_comment','Can add comment');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (26,7,'change_comment','Can change comment');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (27,7,'delete_comment','Can delete comment');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (28,7,'view_comment','Can view comment');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (29,8,'add_notification','Can add notification');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (30,8,'change_notification','Can change notification');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (31,8,'delete_notification','Can delete notification');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (32,8,'view_notification','Can view notification');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (33,9,'add_article','Can add article');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (34,9,'change_article','Can change article');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (35,9,'delete_article','Can delete article');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (36,9,'view_article','Can view article');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (37,10,'add_privatemessage','Can add private message');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (38,10,'change_privatemessage','Can change private message');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (39,10,'delete_privatemessage','Can delete private message');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (40,10,'view_privatemessage','Can view private message');
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq" ON "accounts_customuser_groups" (
	"customuser_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "accounts_customuser_groups_customuser_id_bc55088e" ON "accounts_customuser_groups" (
	"customuser_id"
);
CREATE INDEX IF NOT EXISTS "accounts_customuser_groups_group_id_86ba5f9e" ON "accounts_customuser_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "accounts_customuser_user_permissions_customuser_id_permission_id_9632a709_uniq" ON "accounts_customuser_user_permissions" (
	"customuser_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "accounts_customuser_user_permissions_customuser_id_0deaefae" ON "accounts_customuser_user_permissions" (
	"customuser_id"
);
CREATE INDEX IF NOT EXISTS "accounts_customuser_user_permissions_permission_id_aea3d0e5" ON "accounts_customuser_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "chat_article_author_id_a87727bc" ON "chat_article" (
	"author_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "chat_article_likes_article_id_customuser_id_72f2b2fb_uniq" ON "chat_article_likes" (
	"article_id",
	"customuser_id"
);
CREATE INDEX IF NOT EXISTS "chat_article_likes_article_id_687415ee" ON "chat_article_likes" (
	"article_id"
);
CREATE INDEX IF NOT EXISTS "chat_article_likes_customuser_id_56ff4ac3" ON "chat_article_likes" (
	"customuser_id"
);
CREATE INDEX IF NOT EXISTS "chat_comment_article_id_9e118e55" ON "chat_comment" (
	"article_id"
);
CREATE INDEX IF NOT EXISTS "chat_comment_author_id_ac8b0490" ON "chat_comment" (
	"author_id"
);
CREATE INDEX IF NOT EXISTS "chat_comment_parent_id_cabf04fc" ON "chat_comment" (
	"parent_id"
);
CREATE INDEX IF NOT EXISTS "chat_notification_recipient_id_9a1b369b" ON "chat_notification" (
	"recipient_id"
);
CREATE INDEX IF NOT EXISTS "chat_privatemessage_recipient_id_a7f24d75" ON "chat_privatemessage" (
	"recipient_id"
);
CREATE INDEX IF NOT EXISTS "chat_privatemessage_sender_id_2db5f8ee" ON "chat_privatemessage" (
	"sender_id"
);
COMMIT;
