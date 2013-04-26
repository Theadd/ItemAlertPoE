## ItemAlertPoE — Item Alerter for Path of Exile

**ItemAlertPoE** tracks all item drops in the game [Path of Exile](http://www.pathofexile.com/) and announces them by playing a sound telling you which kind of item it is.
Only valuable items are being annonunced. For example, when a superior gem gets dropped you will hear "Superior Gem" as a fastened voice. To get used with rare sound drops, listen to sounds folder first.

## Notes

Original author: <a href="http://www.ownedcore.com/forums/members/69674-sku.html">SKU</a> / <a href="https://github.com/zku">ZKU</a><br>
PoERecvOffsetFinder.exe author: <a href="http://www.ownedcore.com/forums/members/917705-spl3en.html">Spl3en</a> (<a href="http://spl3en.alwaysdata.net/src/C/PoeOffsetFinder/">Source</a>)

(Original author notes)
It has been brought to my attention that under certain circumstances, my way of processing the packet may be wrong.  
I would strongly advise against using this program on a hardcore character, as crashes may occur.

## List of updates since project fork
* **Unique** items detection (plays unique.wav)
* **Superior Gem** detection (plays superiorgem.wav)
* Non filtered items play sound drop.wav
* Added Multistrike Support Gem
* Added Cyclone Skill Gem
* Removed scrolls from beeping
* Bugfix: Now works with no C:\Windows OS installations

## Installation instructions
* Download and install Python 2.7 (<a href="http://www.python.org/ftp/python/2.7.4/python-2.7.4.msi">link</a>)
* Download and install dependencies (<a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/sjx8sj6u/pydbg-1.2.win32-py2.7.exe">link</a>)
* Download and uncompress ItemAlertPoE anywhere (<a href="https://github.com/Theadd/ItemAlertPoE/archive/master.zip">link</a>)
* Run Path of Exile game client
* Double click src\PoERecvOffsetFinder.exe to make ItemAlertPoE.py work with your current Path of Exile version.
* Finally, double click ItemAlertPoE.py

## Sample output

<p align="center">
  <img src="https://github.com/zku/ItemAlertPoE/blob/master/img/sample.png?raw=true" alt="Sample output"/>
</p>