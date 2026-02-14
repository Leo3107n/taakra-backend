# Generated migration to sync Competition model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_competition_registration'),
    ]

    operations = [
        # Add description to Category
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        # Remove old deadline field
        migrations.RemoveField(
            model_name='competition',
            name='deadline',
        ),
        # Add new date fields
        migrations.AddField(
            model_name='competition',
            name='start_date',
            field=models.DateTimeField(default='2026-01-01T00:00:00Z'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competition',
            name='end_date',
            field=models.DateTimeField(default='2026-12-31T00:00:00Z'),
            preserve_default=False,
        ),
        # Add registrations_count
        migrations.AddField(
            model_name='competition',
            name='registrations_count',
            field=models.IntegerField(default=0),
        ),
        # Make prize optional
        migrations.AlterField(
            model_name='competition',
            name='prize',
            field=models.CharField(blank=True, max_length=200),
        ),
        # Rename Registration.created_at to registered_at
        migrations.RenameField(
            model_name='registration',
            old_name='created_at',
            new_name='registered_at',
        ),
    ]
