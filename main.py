#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email -- make.fun bounty entry.

Brief: one single line of plain text, at most 200 characters, one joke about
a meeting that should have been an email. No code, no attachments, no second
line. The joke must land on its own with no setup, the turn must be fresh,
and every word must earn its place.

Candidate shortlist (hand-written, scored out of 15: self-contained / fresh
turn / every word earns its place):

 1. "We spent an hour in a meeting to decide we needed another meeting, and
    the only action item was scheduling the meeting about the meeting."
    3/2/3 = 8 -- "meeting about the meeting" is a tired trope.
 2. "This meeting could have been an email, but then nobody would have read
    it either -- they'd just have forwarded it to a meeting."
    4/4/4 = 12 -- good twist, but "forwarded it to a meeting" is a stretch.
 3. "Forty-five minutes, nine people, one decision: to send an email
    summarising the meeting that should have been the email."
    5/3/4 = 12 -- clean loop, but the turn is familiar.
 4. "I took 40 minutes of notes in a meeting whose entire outcome fits in
    the subject line: 'Per my last email.'"
    5/4/5 = 14 -- sharp, concrete, the email already existed.
 5. "The meeting ended with everyone agreeing to email each other the things
    we just spent an hour saying out loud."
    5/3/4 = 12 -- solid, but plain.
 6. "Somewhere between 'quick sync' and hour two, we all realised the email
    had already said everything -- we just hadn't read it."
    4/4/4 = 12 -- relatable, slightly wordy.
 7. "The agenda was one line. The meeting was ninety minutes. The email it
    produced was the agenda, forwarded."
    5/5/5 = 15 -- first draft of the winner. Three-beat compression: 1 line /
    90 min / the output is the input, forwarded. But the last clause is
    clunky: "produced" is flat and "forwarded" dangles.
 8. "I joined a meeting to discuss an email, left with an action item to
    email about the meeting, and the email is now scheduling another meeting."
    4/3/3 = 10 -- recursive but convoluted.
 9. "Nine people, one hour, zero decisions -- and the follow-up email just
    says 'great discussion, let's circle back next week.'"
    5/3/4 = 12 -- "circle back" is a cliche kicker.
10. "The meeting that should have been an email ended with a decision to
    have another meeting, which will also produce an email nobody will read."
    4/3/4 = 11 -- "nobody will read" is a decent kicker, setup-heavy.
11. "We spent an hour deciding nothing, then someone said 'I'll send a
    recap email' -- the recap was the meeting, and the meeting was the recap."
    4/4/3 = 11 -- clever identity loop, one clause too many.
12. "An hour-long meeting about an email I already sent, attended by people
    who hadn't read it, ended with a request for me to resend it."
    5/4/4 = 13 -- strong kicker ("resend it"), runner-up.

Revision (second pass on candidate 7): the first draft's last clause dragged.
Compressed the three beats into parallel fragments, gave the punchline an
em-dash beat, and let one small word -- "just" -- carry the whole shrug:
"One-line agenda, ninety-minute meeting -- and the follow-up email was just
the agenda, forwarded." 98 characters. The meeting's entire output is its
own input, merely forwarded; nothing in the line is spare.

Running this script prints exactly that one line.
"""

ENTRY = (
    "One-line agenda, ninety-minute meeting -- and the follow-up email "
    "was just the agenda, forwarded."
)


def main() -> None:
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    print(ENTRY)


if __name__ == "__main__":
    main()
