from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

insults = [
   "you walk into conversations like a pop-up ad nobody asked for.",

"you have the emotional depth of a loading screen.",

"you're somehow loud and irrelevant at the same time.",

"you look like you lose arguments to automatic doors.",

"your existence feels like a software bug in reality.",

"you bring the same energy as wet socks and traffic jams.",

"you're the reason group projects have trust issues.",

"you talk with so much confidence for someone consistently wrong.",

"you could ruin a free vacation with your personality alone.",

"you have the survival instincts of a moth near a flamethrower.",

"you make awkward silence feel comforting.",

"your self-awareness is on airplane mode permanently.",

"you somehow make disappointment look athletic.",

"you're built like a bad decision made at 2am.",

"you look like you ask obvious questions in tutorials.",

"your personality feels factory reset.",

"you radiate 'forwarded without reading' energy.",

"you'd lose a race against common sense.",

"you have the social awareness of a shopping cart with one broken wheel.",

"you make people check their phones mid-conversation out of survival instinct.",

"you look like your favorite hobby is being confidently incorrect.",

"your brain treats critical thinking like a subscription service.",

"you're not mysterious. people just stop caring halfway through.",

"you somehow make every room feel longer.",

"you argue like facts personally offended you.",

"your life decisions look randomly generated.",

"you have the charisma of expired milk.",

"you look like the type to clap when the plane lands.",

"you're the human version of low battery anxiety.",

"your face says 'i ask for the manager' without speaking.",

"you carry yourself like a motivational quote written by someone unemployed.",

"you look like your biggest achievement was surviving high school group chats.",

"you have the vibe of someone who says 'trust me bro' before disaster happens.",

"you make confidence look like a medical condition.",

"you're what happens when overthinking and underperforming combine.",

"you somehow make every joke feel like a hostage situation.",

"you look like your phone storage is 90% screenshots you'll never use.",

"your personality could be replaced by elevator music and nobody would notice.",

"you give people secondhand embarrassment in real time.",

"you look like you still type with one finger under pressure.",

"your presence has the same effect as accidentally stepping in water with socks on.",

"you treat basic responsibilities like optional side quests.",

"you look like you start drama then act confused about consequences.",

"your attention span loses fights against ceiling fans.",

"you have the rare ability to make simple things exhausting.",

"you look like you believe every fake quote on the internet.",

"you somehow turned being average into a full-time personality.",

"you make people regret asking 'how are you?'",

"your confidence survives entirely because reality hasn't caught up yet.",

"you look like you blame technology when you forget your own password."
"you look like your thoughts need buffering.",

"your personality has the nutritional value of cardboard.",

"you somehow make confidence look embarrassing.",

"you walk like your bones are arguing with each other.",

"you bring chaos to things that already worked perfectly fine.",

"you look like you lose staring contests to mirrors.",

"your excuses deserve their own documentary series.",

"you have the decision-making skills of a sleep-deprived raccoon.",

"you radiate the energy of unfinished homework.",

"you look like you still ask if the teacher collected assignments.",

"your opinions feel AI-generated in the worst way possible.",

"you somehow turn every conversation into community service.",

"you look like you chew loudly in quiet rooms.",

"your brain treats logic like a rumor.",

"you have the vibe of someone who forwards fake news confidently.",

"you look like your favorite phrase is 'wait what happened?'",

"your face says 'i definitely clicked the suspicious link.'",

"you move through life like a browser with 97 tabs open.",

"you make bad timing look intentional.",

"your personality feels sponsored by poor decisions.",

"you look like you trip over invisible objects regularly.",

"you have the emotional stability of a shopping cart downhill.",

"you somehow make silence uncomfortable.",

"you look like your alarm clock is your greatest enemy.",

"you have the reaction speed of expired mayonnaise.",

"your stories take longer than necessary and still go nowhere.",

"you give off strong 'battery at 1%' energy.",

"you look like your main talent is misunderstanding situations.",

"your confidence is entirely unsupported by evidence.",

"you somehow manage to disappoint expectations nobody even had.",

"you look like your search history would explain everything.",

"your personality could be replaced by a blinking cursor.",

"you make basic tasks feel like boss fights.",

"you look like someone who forgets why they entered a room every time.",

"your social skills were clearly assembled without instructions.",

"you argue with the confidence of someone who never fact-checks.",

"you look like your favorite activity is standing in the way.",

"you somehow make every situation slightly worse.",

"your vibe screams 'unskippable ad.'",

"you look like you breathe directly into microphones.",

"you bring the same atmosphere as slow internet.",

"you look like your hobbies include missing obvious hints.",

"your logic deserves its own warning label.",

"you somehow make being annoying look effortless.",

"you look like you clap off-beat proudly.",

"your personality feels aggressively average.",

"you move through life like autocorrect gave up on you.",

"you look like you think chain messages actually work.",

"your entire presence feels like unnecessary paperwork.",

"you somehow make simple instructions look impossible.",

"you look like you still fall for obvious scams.",

"your brain runs on trial-version common sense.",

"you have the same energy as a cracked phone screen.",

"you look like you ask questions during movies constantly.",

"your attention span could lose to a spinning ceiling fan.",

"you somehow make every joke sound accidental.",

"you look like your biggest enemy is basic planning.",

"your personality feels heavily recycled.",

"you have the awareness of a traffic cone.",

"you look like your ringtone is still the default one.",

"you somehow make elevators awkward.",

"your vibe says 'reply-all accident waiting to happen.'",

"you look like your favorite app is the calculator.",

"your social battery somehow drains everyone else's too.",

"you make confusion look like a lifestyle choice.",

"you look like your passwords are all variations of 'password123.'",

"your brain treats consequences like optional DLC.",

"you somehow make optimism regret itself.",

"you look like you stand too close while talking.",

"your personality has pop-up ad energy.",

"you make every group chat weaker by existing in it.",

"you look like your greatest achievement was finding the caps lock key.",

"your logic feels like it was assembled during turbulence.",

"you somehow lose arguments against yourself.",

"you look like your thoughts arrive one business day late.",

"your vibe is incredibly uninstallable.",

"you make overexplaining feel like psychological warfare.",

"you look like you say 'long story short' before talking for 40 minutes.",

"your brain runs like a laptop at 2% battery.",

"you somehow make waiting rooms more depressing.",

"you look like you think every motivational quote is deep.",

"your personality feels generated from random leftovers.",

"you bring absolutely nothing to the table except volume.",

"you look like your favorite hobby is misunderstanding sarcasm.",

"your entire existence feels mildly inconvenient.",

"you somehow turn confidence into a public safety issue.",

"you look like your screen time report scares even you.",

"your thoughts move like traffic during construction.",

"you have the timing of a fire alarm at a wedding.",

"you look like your best ideas happen accidentally.",

"your vibe is one missed nap away from disaster.",

"you somehow make incompetence look ambitious.",

"you look like your life updates come with apology notes.",

"your presence lowers the room's collective focus.",

"you somehow make every plan harder than it needed to be.",

"you look like your personality was copied from comment sections.",

"your confidence-to-skill ratio needs government regulation.",

"you bring the same joy as mandatory software updates.",

"you look like your notifications are mostly ignored.",

"your personality could be summarized as 'loading...'",

"you somehow make every explanation sound less believable.",

"you look like your main contribution is making people tired.",

"your vibe screams 'accidentally muted in important meetings.'",

"you have the strategic thinking of spilled soup.",

"you somehow make indecision competitive.",

"you look like your plans fail during the planning stage.",

"your brain treats common sense like premium content.",

"you look like your biggest talent is bad timing.",

"your personality has buffering wheel energy.",

"you somehow make eye contact feel aggressive.",

"you look like your internal monologue is mostly confusion.",

"your presence feels like a low-quality repost.",

"you somehow turned awkwardness into cardio.",

"you look like your favorite exercise is avoiding responsibility.",

"your vibe is one typo away from complete collapse.",

"you somehow make mediocrity look exhausting.",

"you look like your opinions come from random internet polls.",

"your personality is basically a delayed notification.",

"you somehow make every room less productive.",

"you look like your brain still uses internet explorer.",

"your existence feels oddly downloadable.",

"you somehow turned basic communication into a side quest."

]

@app.get("/", response_class=HTMLResponse)
def roast():
    insult = random.choice(insults)
    return f"""
    <html>
        <head><title>meanie</title></head>
        <body style="background:#111; color:#ff4444; font-family:monospace; 
                     display:flex; align-items:center; justify-content:center; 
                     height:100vh; margin:0; text-align:center; padding:20px;">
            <h1>{insult}</h1>
        </body>
    </html>
    """