# Generated by Django 3.2.5 on 2021-12-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dsfr", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dsfrconfig",
            name="accessibility_status",
            field=models.CharField(
                choices=[
                    ("FULL", "complètement"),
                    ("PART", "partiellement"),
                    ("NOT", "non"),
                ],
                default="NOT",
                max_length=4,
                verbose_name="Statut de conformité de l’accessibilité",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="footer_brand",
            field=models.CharField(
                blank=True,
                default="République française",
                max_length=200,
                verbose_name="Institution (pied)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="footer_brand_html",
            field=models.CharField(
                blank=True,
                default="République<br />française",
                max_length=200,
                verbose_name="Institution avec césure (pied)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="footer_description",
            field=models.TextField(blank=True, default="", verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="header_brand",
            field=models.CharField(
                blank=True,
                default="République française",
                max_length=200,
                verbose_name="Institution (en-tête)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="header_brand_html",
            field=models.CharField(
                blank=True,
                default="République<br />française",
                max_length=200,
                verbose_name="Institution avec césure (en-tête)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="site_tagline",
            field=models.CharField(
                blank=True,
                default="Sous-titre du site",
                max_length=200,
                verbose_name="Sous-titre du site",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="site_title",
            field=models.CharField(
                blank=True,
                default="Titre du site",
                max_length=200,
                verbose_name="Titre du site",
            ),
        ),
    ]
