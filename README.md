Users of findagrave.com post requests for photos of gravesites at various cemeteries for display on the site and viewing by relatives and genealogists. Volunteers then fulfill these requests.  Fulfillment of outstanding requests could be accomplished faster if the volunteer could work systematically, photographing multiple requested graves in geographic order. The existing request lists, downloadable as .csv, feature free-text, but reasonably consistent plot coordinates in a single column. This script takes the request .csv for a cemetery, attempts to remove all but section, row, and lot numbers from the 'plot' column and creates 3 new columns to hold them. Then records are then sorted by column, first by section, then row, then lot.

This script is run from the command line using python3. You'll need the pandas and re modules for python as well.  To use it, find a cemetery you're interested in on findagrave and download the requests list in .csv format.  Place that file in the same directory as this script.  Then run this script, redirecting the output to a .txt file for viewing.   

Ex.
python3 groupRequests.py > output.txt 

Let me know if you have any questions.