# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 19:45
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20180111_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcommunity',
            name='approved_license',
            field=models.BooleanField(default=False, help_text='I assert that all Outreachy internship projects under my community will be released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='proprietary_software_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If any internship project under your community furthers the interests of proprietary software, please explain.'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='unapproved_license_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If your community uses a license that is not an OSI-approved and FSF-approved license OR a Creative Commons license, please provide a description and links to the non-free licenses.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='approved_license',
            field=models.BooleanField(default=False, help_text='I assert that this Outreachy internship projects will released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.AlterField(
            model_name='project',
            name='proprietary_software_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If this internship project furthers the interests of proprietary software, please explain.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='unapproved_license_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If this Outreachy internship project will be released under a license that is not an OSI-approved and FSF-approved license OR a Creative Commons license, please provide a description and links to the non-free licenses.'),
        ),
    ]