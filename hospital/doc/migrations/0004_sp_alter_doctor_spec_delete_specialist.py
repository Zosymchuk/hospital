# Generated by Django 4.0 on 2021-12-28 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_specialist_alter_doctor_spec'),
    ]

    operations = [
        migrations.CreateModel(
            name='sp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('cpecializations', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.sp'),
        ),
        migrations.DeleteModel(
            name='specialist',
        ),
    ]