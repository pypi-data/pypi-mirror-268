System.register(["./sentry-legacy.3.5.5.dev18489.js","vue","./_commonjsHelpers-legacy.3.5.5.dev18489.js"],(function(e,r){"use strict";var t;return{setters:[function(e){t=e.at},null,null],execute:function(){var r={words:{m:["један минут","једног минута"],mm:["%d минут","%d минута","%d минута"],h:["један сат","једног сата"],hh:["%d сат","%d сата","%d сати"],d:["један дан","једног дана"],dd:["%d дан","%d дана","%d дана"],M:["један месец","једног месеца"],MM:["%d месец","%d месеца","%d месеци"],y:["једну годину","једне године"],yy:["%d годину","%d године","%d година"]},correctGrammarCase:function(e,r){return e%10>=1&&e%10<=4&&(e%100<10||e%100>=20)?e%10==1?r[0]:r[1]:r[2]},relativeTimeFormatter:function(e,t,m,a){var _=r.words[m];if(1===m.length)return"y"===m&&t?"једна година":a||t?_[0]:_[1];var i=r.correctGrammarCase(e,_);return"yy"===m&&t&&"%d годину"===i?e+" година":i.replace("%d",e)}},m=e("default",{name:"sr-cyrl",weekdays:"Недеља_Понедељак_Уторак_Среда_Четвртак_Петак_Субота".split("_"),weekdaysShort:"Нед._Пон._Уто._Сре._Чет._Пет._Суб.".split("_"),weekdaysMin:"не_по_ут_ср_че_пе_су".split("_"),months:"Јануар_Фебруар_Март_Април_Мај_Јун_Јул_Август_Септембар_Октобар_Новембар_Децембар".split("_"),monthsShort:"Јан._Феб._Мар._Апр._Мај_Јун_Јул_Авг._Сеп._Окт._Нов._Дец.".split("_"),weekStart:1,relativeTime:{future:"за %s",past:"пре %s",s:"неколико секунди",m:r.relativeTimeFormatter,mm:r.relativeTimeFormatter,h:r.relativeTimeFormatter,hh:r.relativeTimeFormatter,d:r.relativeTimeFormatter,dd:r.relativeTimeFormatter,M:r.relativeTimeFormatter,MM:r.relativeTimeFormatter,y:r.relativeTimeFormatter,yy:r.relativeTimeFormatter},ordinal:function(e){return e+"."},formats:{LT:"H:mm",LTS:"H:mm:ss",L:"D. M. YYYY.",LL:"D. MMMM YYYY.",LLL:"D. MMMM YYYY. H:mm",LLLL:"dddd, D. MMMM YYYY. H:mm"}});t.locale(m,null,!0)}}}));
