from django.db import models
import datetime
from django.utils.translation import gettext as _
from datetime import date
from datetime import timedelta as tdelta
from django.utils import timezone
import calendar


# Create your models here.
class Post(models.Model):
    CONTROL_REVENUE_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    CONTROL_REVENUE = models.TextField(null=False, db_column='ctrlrevenue', default=1, choices=CONTROL_REVENUE_CHOICES)

    CONTROL_CATEGORY_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    CONTROL_CATEGORY = models.CharField(max_length=8,blank=False,null=True,db_column='ctcat', choices=CONTROL_CATEGORY_CHOICES, default=1)

    GROUP_NAME_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    GROUP_NAME =  models.CharField(max_length=8,blank=False,null=True,db_column='gname', choices=GROUP_NAME_CHOICES, default=1)

    ACCOUNT_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    ACCOUNT = models.CharField(max_length=8,blank=False,null=True, db_column='accnt', choices=ACCOUNT_CHOICES, default=1 )

    ACCOUNT_NUMBER_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    ACCOUNT_NUMBER = models.CharField(max_length=100, null=True, blank=False, db_column='accnum', choices=ACCOUNT_NUMBER_CHOICES, default=1)

    INVOICE_NUMBER_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    INVOICE_NUMBER = models.TextField(null=False, db_column='invcnum', choices=INVOICE_NUMBER_CHOICES, default=1)

    COUNTRY_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    COUNTRY = models.CharField(max_length=100, null=True, blank=False,db_column='ctry', choices=COUNTRY_CHOICES, default=1 )
    CITY_STATE_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
    CITY_STATE = models.CharField(max_length=6, choices=CITY_STATE_CHOICES, default='green')

    A_SITE_ADDRESS_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    A_SITE_ADDRESS = models.CharField(max_length=100, null=True, blank=True, db_column='siteaddr', choices=A_SITE_ADDRESS_CHOICES, default=1)

    PRODUCT_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    PRODUCT = models.CharField(max_length=100, null=True, blank=True, db_column='prdchoices', choices=PRODUCT_CHOICES, default=1)

    SERVICE_CATEGORY_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    SERVICE_CATEGORY = models.CharField(max_length=100, null=True, blank=True, db_column='servcat', choices=SERVICE_CATEGORY_CHOICES, default=1)

    CLASSIC_SITE_ID_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    CLASSIC_SITE_ID = models.CharField(max_length=100, null=False, blank=True, db_column='classiteid', choices=CLASSIC_SITE_ID_CHOICES, default=1)

    SERVICE_PERIOD_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    SERVICE_PERIOD = models.TextField(null=True, blank=False, db_column='servprd', choices=SERVICE_PERIOD_CHOICES, default=1)

    USF_CODE_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    USF_CODE = models.CharField(max_length=100, null=True, blank=False, db_column='usfcde', choices=USF_CODE_CHOICES, default=1 )

    SUPPLIER_NAME_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    SUPPLIER_NAME = models.CharField(max_length=100, null=True, blank=False, db_column='spprnme', choices=SUPPLIER_NAME_CHOICES, default=1)

    SUPPLIER_CIRCUIT_ID_1_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    SUPPLIER_CIRCUIT_ID_1 = models.CharField(max_length=100, null=True, blank=False, db_column='sprcid1', choices=SUPPLIER_CIRCUIT_ID_1_CHOICES, default=1)

    SUPPLIER_CIRCUIT_ID_2_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    SUPPLIER_CIRCUIT_ID_2 = models.CharField(max_length=100, null=True, blank=False, db_column='sprcid2', choices=SUPPLIER_CIRCUIT_ID_2_CHOICES, default=1)

    SUPPLIER_BAN_1_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    SUPPLIER_BAN_1 = models.TextField(null=False, db_column='sprban1', choices=SUPPLIER_BAN_1_CHOICES, default=1)

    SUPPLIER_BAN_2_CHOICES = (
    ('1','1'),
    ('2', '2'),
)
    SUPPLIER_BAN_2 = models.CharField(max_length=100, null=True, blank=False, db_column='sprban2', choices=SUPPLIER_BAN_2_CHOICES, default=1)
