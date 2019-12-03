# Shelvd (Shelv? Litshelf? whatever)
### A Goodreads clone or competitor
#### or, a lesson in Svelte


Inspired by a very nice article I found on HN:
[Almost Everything About Goodreads is
Broken](https://onezero.medium.com/almost-everything-about-goodreads-is-broken-662e424244d5)

### Notes from reading the HN discussion:

- A not-bad book recommendation engine: [Now, what do I read?](https://nowwhatdoiread.com/)

- A rating algorithm, [rate.house](https://rate.house/) written by
[ztarven](https://news.ycombinator.com/user?id=ztarven) that uses community
upvotes for suggestions.

- Some people say [Criticker](https://www.criticker.com/) is great for movie
recommendations.

- [kamilszybalski](https://news.ycombinator.com/user?id=kamilszybalski),
  [twitter](https://twitter.com/KamilSzybalski) says: "I once worked for a
startup where we attempted this, in a sense. We built an app that let users
take a picture of their bookshelf, we scanned the spines then digitized your
"Shelfie". Our pitch was that we would give you the ebook of the print book
that you own either for free or at a deep discount...Simplified, [our
recommendation engine worked such that] if you have actual photos of
bookshelves it's easy to start building recommendations. Person a read a,b,c,
person b also read a,b,c, however, person a read e,f so maybe person b would
also like e and f."

- There is a Goodreads API, so one could potentially build a migration tool for
  Goodreads users.

- [Bookdigits](https://bookdigits.com/) exists, but it doesn't look that much better..

- [helloreads](https://www.helloreads.com/) is another attempt to unseat
  Goodreads, but development is on hold

- [LibraryThing](https://www.librarything.com/), another one.

- [adwf](https://news.ycombinator.com/user?id=adwf) has an interesting point about stop word filtering:
>In both cases in the article it's almost certainly down to "stop word"
>removal.
>
>The titles contain "the" and "and". These kind of words get filtered out
>because they make indexing incredibly difficult, ie. you search for "the" and
>get every single book containing "the" in the title (and sometimes
>description, depending on how deep the search is). So they exclude extremely
>common words to get eg. "catch kill". Then they have to rank the results for
>"catch kill" by some other heuristic - like popularity - and you get a list of
>books that people weren't looking for. Not to mention the first two books in
>the list were actually exact matches, so maybe they were more popular on the
>site.
>
>Big search engines do try to correct for this, but it's not an easy problem.
>Usually results in some hard-coded exceptions for names like "The Who", but
>it's not trivially scalable.
>
>In the case of your google maps results, I imagine it'll be something like
>(popularity * distance), which isn't necessarily the best heuristic.
>
>The problem is that you can't please everyone with heuristics. Give power
>users the option to adjust the search to distance-first, popularity-first or
>any other of a dozen different combos and you end up with a confusing mess of
>a UI. Simplify it and give them your nicely hand-crafted best guess and there
>will always be someone complaining... 

- [literature-map](https://www.literature-map.com/info.php) is really
  interesting, but the interface is super frustrating. It's based on
[Gnooks](http://www.gnooks.com/). This seems like a possible resource to
leverage. The author is [Marek Gibney](http://www.gnooks.com/about).



- Interesting observations from users:
    - "That's because the recommendation systems are optimizing for the wrong
      things: typically dwell time. You are highly likely to dwell longer on
scifi, so heres more scifi for you!"
    - "Optimizing for novelty is difficult because the set of unknown things is
      much larger than the set of known things. Plus, it is risky from a
business point of view."
    - "the integrations with the kindle go a very long way towards cultivating
      engagement (when you start a book, kindle will update your profile by
default, it'll add your rating, mark the book as finished, all through the
normal ux of the kindle)"

- Feature requests:
    - [mmanfrin](https://news.ycombinator.com/user?id=mmanfrin)"I desperately
      want a feature that'll show me the books most-reviewed among my friends,
or highest reviewed with \>X # of reviews. You can see what individual friends
have reviewed, but there is nothing I've found to aggregate. "
    - (mmanfrin)"More reading stats (right now it shows number of books, and total pages
      at the end of the year). I wanna see breakdowns of categories, authors,
fiction/nonfiction."
    - (mmanfrin)"I had an idea for per-book or per-series wikis that have
      spoiler-bracketed info. E.g., [spoiler b2p300 "King Soandso is murdered
by Assassin Soandso"] would show in a book wiki if you are past book 2, page
\300. I read a bit of fantasy and have a tendency to want to google 'who is x',
but that is fraught with spoilers. This is a feature that could exist as its
own site, but I think it'd be a good companion to a goodreads-esque site."
    - "What I'd really like is more access to the data and filtering mechanisms
      to try to build recommendations for myself."
    - [aklemm](https://news.ycombinator.com/user?id=aklemm)"maybe you could
      bootstrap community/engagement by integrating with public library
catalogs and checkout records? Patrons could opt in to sharing their activity
automatically and the library website could have update options as part of the
checkout management process. Might be a nice little niche entrance into a
customer base there."
    - "What Goodreads is good for is keeping your own list of books you want to
      read or have read this year. It’s a list-making app."
    - [monkeypizza](https://news.ycombinator.com/user?id=monkeypizza)"A feature
      I want on goodreads is "for me and a friend, show me the rarest book we
have read in common"."
