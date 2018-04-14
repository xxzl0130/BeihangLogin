import sys
import re
from datetime import *


def time2str(dt):
    return "%s%s%sT%s%s%s" % (dt.date.year, dt.date.month, dt.date.day, dt.time.hour, dt.time.minute, dt.time.second)


def str2time(st):
    dt = datetime(int(st[0:4]), int(st[4:6]), int(st[6:8]),
                  int(st[9:11]), int(st[11:13]), int(st[13:16]))
    return dt


CALSCALE = "GREGORIAN"
CALNAME = "Curriculum"
TIMEZONE = "Asia/Shanghai"
TZOFFSETFROM = "+0800"
TZOFFSETTO = "+0800"
TZNAME = "CST"
DTSTART = "19700101T000000"
TIMEFORMAT = "%Y%m%dT%H%M%S"

startTime = datetime(2012, 9, 10, 0, 0, 0)

timeList = [[timedelta(hours=h, minutes=0), timedelta(
    hours=h + 1, minutes=0)] for h in range(8, 20)]

weekList = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

weekInSemester = 19
# weekInSemester=int(input())


def output(info, out_path):
    with open(out_path, 'w') as fout:
        # Start to write the output file.
        fout.write("BEGIN:VCALENDAR\n\
        PRODID:-//Google Inc//Google Calendar 70.9054//EN\n\
        VERSION:2.0\n\
        CALSCALE:%s\n\
        METHOD:PUBLISH\n\
        X-WR-CALNAME:%s\n\
        X-WR-TIMEZONE:%s\n\
        X-WR-CALDESC:\n\
        BEGIN:VTIMEZONE\n\
        TZID:%s\n\
        X-LIC-LOCATION:%s\n\
        BEGIN:STANDARD\n\
        TZOFFSETFROM:%s\n\
        TZOFFSETTO:%s\n\
        TZNAME:%s\n\
        DTSTART:%s\n\
        END:STANDARD\n\
        END:VTIMEZONE\n\
        " % (CALSCALE, CALNAME, TIMEZONE, TIMEZONE, TIMEZONE, TZOFFSETFROM, TZOFFSETTO, TZNAME, DTSTART))

        # print(datetime.now())
        # today = time2str(datetime.now())
        today = datetime.now().strftime(TIMEFORMAT)

        for event in schedule:
            fout.write("BEGIN:VEVENT\n")
            fout.write("DTSTART;TZID=%s:%s\n" % (TIMEZONE, (startTime +
                                                            weekDelta + timeList[startUnit - 1][0]).strftime(TIMEFORMAT)))
            fout.write("DTEND;TZID=%s:%s\n" % (TIMEZONE, (startTime + weekDelta +
                                                          timeList[startUnit + units - 2][1]).strftime(TIMEFORMAT)))
            fout.write("RRULE:FREQ=WEEKLY;COUNT=%d;BYDAY=%s\n" %
                       (weekInSemester, weekList[week - 1]))
            fout.write("DTSTAMP%sZ\n" % (today))
            # fout.write("UID")
            fout.write("CREATED:%sZ\n" % (today))
            fout.write("DESCRIPTION:%s\n" %
                       (content[:content.find("<br/>")].replace("<br>", " ")))
            fout.write("LAST-MODIFIED:%sZ\n" % (today))
            fout.write("LOCATION:%s\n" % (content[content.find(
                "<br/>"):].replace("<br>", "").replace("<br/>", " ")))
            fout.write("SEQUENCE:%d\n" % (0))
            fout.write("STATUS:CONFIRMED\n")
            fout.write("SUMMARY:%s\n" %
                       (content[content.find("<br>") + 4:content.find("<br/>")]))
            fout.write("TRANSP:OPAQUE\n")
            fout.write("END:VEVENT\n")

        fout.write("END:VCALENDAR\n")
