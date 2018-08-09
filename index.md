---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Datasets for Visualization Construction
---

This website contains a collection of datasets for visualization construction.

Most datasets are collected from their original sources and processed. Unless otherwise stated, all derived work is shared under the
<a href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)</a> license. <b>Please attribute the original sources when using these datasets.</b>

The primary purpose of this collection is to demonstrate and evaluate visualization construction tools.
Although there was a considerable amount of effort to make these datasets correct and accurate, please be cautious when using them for serious analysis.

For questions or complaints, please email "visualization.datasets [at] gmail.com".

<div class="dataset-list">
{% for item in site.data.datasets %}

<div id="{{ item.id }}" class="dataset-item">
    <div class="el-header">{{ item.name | markdownify }}</div>
    <div class="el-description">
        <div class="el-label">Description</div>
        <div class="el-detail">{{ item.description | markdownify }}</div>
    </div>
    <div class="el-description">
        <div class="el-label">Source</div>
        <div class="el-detail">{{ item.source | markdownify }}</div>
    </div>
    <div class="el-description">
        <div class="el-label">Download</div>
        <ul class="el-detail">
            {% for file in item.files %}
                <li>
                    <a title="Preview" href="show#!{{ file | prepend: 'datasets/' }}"><i class="fas fa-search"></i></a>
                    <a title="Download" href="{{ file | prepend: 'datasets/' }}"><i class="fas fa-download"></i> {{ file }}</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</div>

{% endfor %}
</div>