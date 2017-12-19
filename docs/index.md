---
layout: page
title: DAAD
subtitle: Data Analysis Against Diseases
use-site-title: true
---
The human brain is possibly one of the most complex structures in the universe,
as judged by some human brains. The past few years have seen a huge burst of popularity
of brain-related research. With the prevalence of fMRI research, showing correlations
(_this is your brain on..._) with what generally excites people (sex, food and politics)
 has captured the public imagination. What is important however is
manner.
the public imagination.
## Introduction

Parkinson's disease is caused by a progressive degeneration of certain neural cells of the central nervous systems which are responsible for dopamine production, a chemical used into the brain to allow communication between cells. The loss of dopaminergic function produces drastic changes in brain circuits involved in the execution of voluntary movements. As a consequence, patients slowly start to present motor symptoms such as tremor, rigidity or in general difficulties in movements. In advanced stages, dementia as well as other behavioural problems gradually take the upper hand.


Early diagnosis
Different regions of the brain typically activate together in what neuroscientists call "brain networks". Those networks are used to study brain architecture and function.
Resting state fMRI allows to study the networks that are active when a person is at rest, not performing any particular task. Those networks are typically robust among subjects, while they are destroyed or disorganized as a consequence of several brain diseases, including Parkinson.
Studying how Parkinson's disease affects neural networks could help understanding the mechanisms underlying the pathophysiology of the disorder, allowing early diagnosis and in particular evaluating treatments.
Study the consequences of dopamine loss on the functions of the brain.



# Dataset
One of the missions of the Parkinson's progression markers initiative is to collect advanced imaging data in order to identify
 biomarkers for the evaluation of the disease.
## Dataset


<!-- Uncomment the following to get blog posts, not needed for ADA -->

<!-- <div class="posts-list">
  {% for post in paginator.posts %}
  <article class="post-preview">
    <a href="{{ post.url | prepend: site.baseurl }}">
	  <h2 class="post-title">{{ post.title }}</h2>

	  {% if post.subtitle %}
	  <h3 class="post-subtitle">
	    {{ post.subtitle }}
	  </h3>
	  {% endif %}
    </a>

    <p class="post-meta">
      Posted on {{ post.date | date: "%B %-d, %Y" }}
    </p>

    <div class="post-entry-container">
      {% if post.image %}
      <div class="post-image">
        <a href="{{ post.url | prepend: site.baseurl }}">
          <img src="{{ post.image }}">
        </a>
      </div>
      {% endif %}
      <div class="post-entry">
        {{ post.excerpt | strip_html | xml_escape | truncatewords: site.excerpt_length }}
        {% assign excerpt_word_count = post.excerpt | number_of_words %}
        {% if post.content != post.excerpt or excerpt_word_count > site.excerpt_length %}
          <a href="{{ post.url | prepend: site.baseurl }}" class="post-read-more">[Read&nbsp;More]</a>
        {% endif %}
      </div>
    </div>

    {% if post.tags.size > 0 %}
    <div class="blog-tags">
      Tags:
      {% if site.link-tags %}
      {% for tag in post.tags %}
      <a href="{{ site.baseurl }}/tag/{{ tag }}">{{ tag }}</a>
      {% endfor %}
      {% else %}
        {{ post.tags | join: ", " }}
      {% endif %}
    </div>
    {% endif %}

   </article>
  {% endfor %}
</div>

{% if paginator.total_pages > 1 %}
<ul class="pager main-pager">
  {% if paginator.previous_page %}
  <li class="previous">
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&larr; Newer Posts</a>
  </li>
  {% endif %}
  {% if paginator.next_page %}
  <li class="next">
    <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">Older Posts &rarr;</a>
  </li>
  {% endif %}
</ul>
{% endif %} -->
