# Generated by Django 3.0.3 on 2020-04-20 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('question', '0001_initial'),
        ('exam', '0002_auto_20200401_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='练习名称')),
            ],
        ),
        migrations.CreateModel(
            name='Recode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='你的作答')),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='question.Choice', verbose_name='选择题')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Exercise', verbose_name='练习')),
                ('fill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='question.Fill', verbose_name='填空题')),
                ('judge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='question.Judge', verbose_name='判断题')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='question.Program', verbose_name='编程题')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
        ),
    ]