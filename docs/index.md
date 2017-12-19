---
layout: page
title: DAAD
subtitle: Data Analysis Against Diseases
use-site-title: true
---
The human brain is possibly one of the most complex structures in the universe, as judged by some human brains. The past few years have seen a huge burst of [popularity](https://www.sciencedaily.com/releases/2017/04/170420093736.htm) in brain-related research. With regards to [fMRI](#fmri) based research since its discovery in the 1990s, showing correlations (_this is your brain on ..._) with what generally excites people ([sex](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4782579/), [food](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0131727) and [politics](https://www.nature.com/articles/srep39589)) has captured the public imagination. This has led to [criticism](https://www.newyorker.com/news/news-desk/neuroscience-fiction) about whether such conclusions can be or should be drawn.

<table align="center">
  <caption align="bottom"><a href="https://xkcd.com/1453/">xkcd cracks a joke on fMRI and its effectiveness</a></caption>
  <tr><td><img class="image" src = "img/fmri.png"></td></tr>
</table>

Unfortunately, what has not come too much into the public view is the use of fMRI to understand neurodegenerative diseases in a better way. There is ongoing research into finding early ways of distinguishing patients suffering from  [Alzheimer's disease](https://www.ncbi.nlm.nih.gov/pubmed/20541837), [schizophrenia](https://rd.springer.com/chapter/10.1007/978-3-319-02913-9_52) and [depression](https://peerj.com/preprints/412.pdf).

>Here, we will focus on [Parkinson's Disease](#pd) (henceforth PD) and show how we can use Data Analysis to help in combating it.

* [What is fMRI?](#fmri)
* [What is Parkinson Disease?](#pd)

### <a name="fmri"></a>
### What is fMRI?
Functional magnetic resonance imaging ([fMRI](https://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging)) is a way to measure brain activity indirectly by using the fact that increase in activity in a region of the brain is often coupled with increase in blood flow to that region. It has been widely used by cognitive neuroscientists and psychologists to examine the neural correlates of higher cognitive functions in humans, such as decision-making, emotion regulation, social interactions and consciousness.

### <a name="pd"></a>
### What is Parkinson's Disease?
Parkinson's disease ([PD](https://en.wikipedia.org/wiki/Parkinson%27s_disease)) is a disease caused by a progressive dying of certain cells in the central nervous system responsible for producing a chemical called dopamine, used to allow brain cells to communicate with each other. Their loss produces great changes in the control of voluntary movements. So, patients start showing symptoms like rigidity, tremor (involuntary shaking) or general difficulties in movements. In advanced stages, behavioural problems like dementia also appear




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
