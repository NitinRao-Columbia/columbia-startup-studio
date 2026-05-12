# Freeweight Analytics Snapshot
**April 16, 2026**

---

## 1. Analytics Setup

We are not running GA4 or Amplitude. Our growth channel is exclusively direct outreach — personal emails, in-person conversations with Columbia S&C coaches, and warm introductions through our athlete networks. Paid acquisition and web traffic campaigns are not part of our current strategy, so pageview and session tracking via GA4 would not produce meaningful data at this stage.

We are tracking our funnel through our own `/api/metrics` endpoint and direct observation of user behavior in the product.

Current metrics as of April 16:
```json
{
  "signups": 77,
  "active_users": 8,
  "waitlist": 10,
  "page_views": 0
}
```

---

## 2. Funnel

| Step | Count | Conversion |
|---|---|---|
| Signups | 77 | — |
| Active users (completed at least one meaningful action) | 8 | 10.4% |
| Waitlist | 10 | — |

---

## 3. Written Analysis

**Where is the biggest drop-off?**

The gap between signups and active users is severe. 77 people have created accounts and only 8 have done something meaningful in the product. That is a 90% drop-off between account creation and activation.

**What do we think is causing it?**

Two likely causes. First, a significant portion of our signups are coaches who created accounts after a conversation with us but have not yet gone through the full setup flow — creating a group, building a program, and assigning it to athletes. The coach onboarding requires more steps and more upfront investment than the athlete side, and coaches are busy. Signing up takes thirty seconds; building out a full program takes real time.

Second, athletes cannot do much in the product until their coach has assigned them a program. If a coach signs up but does not complete setup, any athletes they invited are also stuck in a dormant state. The activation of athletes is structurally dependent on coach activation, which means one stalled coach blocks an entire roster.

**What will we do about it?**

Two things. First, we are going to follow up directly with every coach who signed up but has not activated, offer to do a live walkthrough, and help them get their first program built in the session rather than leaving them to do it alone. Second, we are looking at reducing the friction of the initial coach setup — specifically whether we can get a coach to their first assigned workout faster by defaulting them into a simplified program builder rather than the full interface on first login.

The 10 waitlist signups are likely coaches or athletes who heard about the product through word of mouth but have not been formally onboarded yet. We will work through those this week.