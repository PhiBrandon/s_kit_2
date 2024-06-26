# Generated by Django 5.0.6 on 2024-05-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField(null=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('parent_observation_id', models.TextField(null=True)),
                ('type', models.CharField(choices=[('CHOICE1', 'Choice 1'), ('CHOICE2', 'Choice 2')], max_length=50)),
                ('trace_id', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('model', models.TextField(null=True)),
                ('model_parameters', models.JSONField(null=True)),
                ('input', models.JSONField(null=True)),
                ('output', models.JSONField(null=True)),
                ('level', models.CharField(choices=[('DEFAULT', 'Default'), ('ERROR', 'Error')], default='DEFAULT', max_length=50)),
                ('status_message', models.TextField(null=True)),
                ('completion_start_time', models.DateTimeField(null=True)),
                ('completion_tokens', models.IntegerField(default=0)),
                ('prompt_tokens', models.IntegerField(default=0)),
                ('total_tokens', models.IntegerField(default=0)),
                ('version', models.TextField(null=True)),
                ('project_id', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('unit', models.TextField(null=True)),
                ('prompt_id', models.TextField(null=True)),
                ('input_cost', models.DecimalField(decimal_places=30, max_digits=65, null=True)),
                ('output_cost', models.DecimalField(decimal_places=30, max_digits=65, null=True)),
                ('total_cost', models.DecimalField(decimal_places=30, max_digits=65, null=True)),
                ('internal_model', models.TextField(null=True)),
            ],
            options={
                'db_table': 'observations',
                'managed': False,
            },
        ),
    ]
