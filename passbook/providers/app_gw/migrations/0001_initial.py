# Generated by Django 3.0.6 on 2020-05-19 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("oidc_provider", "0026_client_multiple_response_types"),
        ("passbook_core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicationGatewayProvider",
            fields=[
                (
                    "provider_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="passbook_core.Provider",
                    ),
                ),
                ("name", models.TextField()),
                ("internal_host", models.TextField()),
                ("external_host", models.TextField()),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="oidc_provider.Client",
                    ),
                ),
            ],
            options={
                "verbose_name": "Application Gateway Provider",
                "verbose_name_plural": "Application Gateway Providers",
            },
            bases=("passbook_core.provider",),
        ),
    ]
