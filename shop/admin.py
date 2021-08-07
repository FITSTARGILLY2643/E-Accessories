# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


admin.site.register(
    [Admin, Customer, Category, Product, Cart, CartProduct, Order, ProductImage])
