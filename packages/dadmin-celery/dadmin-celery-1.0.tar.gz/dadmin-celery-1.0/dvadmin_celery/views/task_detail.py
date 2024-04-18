# -*- coding: utf-8 -*-

"""
@author: 阿辉
@contact: QQ:2655399832
@Created on: 2022/9/21 16:30
@Remark:
"""
import json
import time
from json import JSONDecoder

from django_celery_results.models import TaskResult
import django_filters
from rest_framework import serializers

from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet




class CeleryTaskDetailSerializer(CustomModelSerializer):
    """定时任务详情 序列化器"""
    class Meta:
        model = TaskResult
        fields = '__all__'

    # def get_result(self, obj):
    #     value = json.loads(obj.result)
    #     return value


class CeleryTaskDetailFilterSet(django_filters.FilterSet):
    date_created = django_filters.BaseRangeFilter(field_name="date_created")
    class Meta:
        model = TaskResult
        fields = ['id', 'status', 'date_done', 'date_created', 'result', 'task_name', 'periodic_task_name']




class CeleryTaskDetailViewSet(CustomModelViewSet):
    """
    定时任务
    """
    queryset = TaskResult.objects.all()
    serializer_class = CeleryTaskDetailSerializer
    filter_class = CeleryTaskDetailFilterSet
