"""
Copyright (C) 2024, Pelican Project, Morgridge Institute for Research
 
Licensed under the Apache License, Version 2.0 (the "License"); you
may not use this file except in compliance with the License.  You may
obtain a copy of the License at
 
    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
"""


"""
Code to parse the headers returned by a GET call to the director
"""
def parse_metalink(headers={}):
    """
    Parse the metalink headers to get a list of caches to attempt to try in priority orider
    """
    linkPrio = []

    if "Link" in headers:
        links = headers["Link"].split(",")
        for mlink in links:
            elmts = mlink.split(";")
            mdict = {}
            for elm in elmts[1:]:
                left, right = elm.split("=", 1)
                mdict[left.strip()] = right.strip()
            
            priority = len(headers)
            if mdict["pri"]:
                priority = int(mdict["pri"])
            
            link = elmts[0].strip(" <>")

            linkPrio.append([link, priority])

    linkPrio.sort(key=lambda x: x[1])
    return linkPrio

def get_dirlist_loc(headers={}):
    """
    Parse the headers to get the dirlist location

    This will None if there is no dirlist location
    """
    if "X-Pelican-Namespace" in headers:
        namespace = headers["X-Pelican-Namespace"]
        elmts = namespace.split(", ")
        for elm in elmts:
            left, right = elm.split("=", 1)
            if left == "collections-url":
                return right
        
    
    return None