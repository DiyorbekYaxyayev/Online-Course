from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_teachers_delete_courseuser'),
    ]

    operations = [
        # Avval ustunni vaqt satr sifatida saqlash uchun CharField qilib o'zgartiramiz
        migrations.AlterField(
            model_name='lesson',
            name='video_duration',
            field=models.CharField(max_length=8, default="00:00:00"),
        ),
        # Keyin uni TimeField ga o'zgartiramiz
        migrations.AlterField(
            model_name='lesson',
            name='video_duration',
            field=models.TimeField(),
        ),
    ]
