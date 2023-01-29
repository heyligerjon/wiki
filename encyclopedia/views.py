from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

import markdown2
from random import choice
from . import util

class SearchForm(forms.Form):
  search = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search Wiki'}))

searchForm = SearchForm(auto_id=True)

class NewPageForm(forms.Form):
  title = forms.CharField()
  markdown = forms.CharField(widget=forms.Textarea)

def index(request):
  if request.method == "POST":
    form = NewPageForm(request.POST)

    if form.is_valid():
      form = form.cleaned_data
      title = form["title"]
      print(form)
      markdown = form["markdown"]
      util.save_entry(title, markdown)

    return render(request, "encyclopedia/index.html", {
      "entries": util.list_entries(),
      "searchbox": searchForm
    })
  else:
    return render(request, "encyclopedia/index.html", {
      "entries": util.list_entries(),
      "searchbox": searchForm
    })

def page(request, entry):
  page = util.get_entry(entry)
  if page is None:
    return render(request, "encyclopedia/error.html", {
      "error": "Page Does Not Exist",
      "message": "This page could not be found",
      "searchbox": searchForm
    })
  else:
    return render(request, "encyclopedia/page.html", {
      "page": markdown2.markdown(page),
      "title": entry,
      "searchbox": searchForm
    })

def search(request):
  if request.method == "POST":
    form = SearchForm(request.POST)

    if form.is_valid():
      search = form.cleaned_data["search"]
      entries = util.get_entry(search)

      if entries == None:
        p = list()
        entries = util.list_entries()
        for entry in entries:
          if search.lower() in entry.lower():
            p.append(entry)

        p.sort()
        entries = p
        return render(request, "encyclopedia/searchresults.html", {
        "query": search,
        "entries": entries,
        "searchbox": searchForm
        })
      else:
        return HttpResponseRedirect(reverse("wiki:page", kwargs={"entry": search}))
    else:
      return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "searchbox": searchForm
      })

def newPage(request):
  newForm = NewPageForm(auto_id=True)

  return render(request, "encyclopedia/new.html", {
    "searchbox": searchForm,
    "form": newForm
  })

def edit(request, entry):
  markdown = util.get_entry(entry)
  page = markdown2.markdown(markdown)
  if request.method == "GET":
    editForm = NewPageForm({
      'markdown': markdown,
      'title': entry
    })

    if editForm.is_valid():
      editForm.markdown = markdown
      
      return render(request, "encyclopedia/edit.html", {
          "edit": editForm,
          "title": entry,
          "searchbox": searchForm
        })
    else: 
      return render(request, "encyclopedia/page.html", {
        "page": markdown2.markdown(page),
        "title": entry,
        "searchbox": searchForm
      })

def random(request):
  entries_list = util.list_entries()
  rand_entry = choice(entries_list)

  return HttpResponseRedirect(reverse("wiki:page", kwargs={"entry": rand_entry}))