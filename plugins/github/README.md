```
The q search term can also contain any combination of the supported code search qualifiers as described by the in-browser code search documentation and search syntax documentation:

in Qualifies which fields are searched. With this qualifier you can restrict the search to the file contents (file), the file path (path), or both.
language Searches code based on the language it's written in.
fork Specifies that code from forked repositories should be searched (true). Repository forks will not be searchable unless the fork has more stars than the parent repository.
size Finds files that match a certain size (in bytes).
path Specifies the path prefix that the resulting file must be under.
filename Matches files by a substring of the filename.
extension Matches files with a certain extension after a dot.
user or repo Limits searches to a specific user or repository.
```
https://developer.github.com/v3/search/#search-code
Basic authentication