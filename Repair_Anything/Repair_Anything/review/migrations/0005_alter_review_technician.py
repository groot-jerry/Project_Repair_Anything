# Generated by Django 5.0.1 on 2024-05-02 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_technician_id_utechnicianprofile'),
        ('review', '0004_review_technician_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='account.technicianprofile'),
        ),
    ]
