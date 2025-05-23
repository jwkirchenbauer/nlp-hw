
This first homework will be relatively easy.  The most important parts
of this homework are to understand how I do homeworks for the course,
my coding style, and the level of coding required for the course.

But we still want to do something relevant to the material of the
course, so we'll be computing [tf-idf
representations](https://onlinelibrary.wiley.com/doi/full/10.1002/bult.274)
of documents.


What to Do
=============

# Code (20 Points)

You'll need to complete several functions in the TfIdf class:
* constructor
* train_seen
* finalize
* add_document
* term_freq
* inv_docfreq

I'll talk about each of these and what you have to do for them.  Each
of these should be fairly easy to do.  If you find yourself spending
hours on one of these, you're probably overthinking it or doing
something that Python can do for you.

They're listed roughly in the order that you should complete them, but
you obviously need to think about all of them first before you can
start.

constructor
--------------

You don't need to do too much here except for creating datastructures
that you may need to count things up later.  I'd suggest taking a look
at NLTK's
[FreqDist](http://www.nltk.org/api/nltk.html?highlight=freqdist) and/or
refresh your memory on Python
[collections](https://docs.python.org/3/library/collections.html).

train_seen
----------

Here, you'll need to take the *string* representations that you've
seen and keep track of how often you've seen them.

finalize
----------

Once we've done a scan over all of the documents, we can create a
vocabulary, taking all of the words that have appeared more than or
equal to unk_cutoff times into the vocabulary.  You make want to free
up the memory you used for train_seen here, but not necessary for
getting a good grade.

The most important thing is that after this function has run, the
vocab data member of TfIdf should map words (in string form) to their
vocabulary id (an integer).

add_document
---------

Take in a document and keep track of the words that you see in
appropriate datastructures so that the next two functions work.

term_freq
----------

Return the frequency of a word.

inv_docfreq
-------------

Return the inverse document frequency of a word.


Write Up (5 Points)
=================

What are words that, specifically for this collection, appear in a lot
of documents and are thus not helpful query terms?

# Submission Instructions


1. Submissions will be made on Gradescope.

2. You will submit a zip file containing your code (tfidf.py) and the PDF for
the write-up. If you check your code against your own test cases, you can add
the file (which will be like test.py) containing your own test cases in the
zip too.

The code will run against the public test cases (the ones you can already see
in the given test.py file) on the server and you can see those results. You
should make sure you pass these cases before the submission deadline.

