text = """If you wanna run away with me, I know a galaxy
And I can take you for a ride
I had a premonition that we fell into a rhythm
Where the music don't stop for life
Glitter in the sky, glitter in my eyes
Shining just the way I like
If you're feeling like you need a little bit of company
You met me at the perfect time

[Pre-Chorus]
You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading
Yeah, yeah, yeah, yeah, yeah
[Chorus]
I got you, moonlight, you're my starlight
I need you all night, come on, dance with me
I'm levitating
You, moonlight, you're my starlight (You're the moonlight)
I need you all night, come on, dance with me
I'm levitating

[Verse 2]
I believe that you're for me, I feel it in our energy
I see us written in the stars
We can go wherever, so let's do it now or never
Baby, nothing's ever, ever too far
Glitter in the sky, glitter in our eyes
Shining just the way we are
I feel like we're forever every time we get together
But whatever, let's get lost on Mars

[Pre-Chorus]
You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading
Yeah, yeah, yeah, yeah, yeah

[Chorus]
I got you, moonlight, you're my starlight
I need you all night, come on, dance with me
I'm levitating
You, moonlight, you're my starlight (You're the moonlight)
I need you all night, come on, dance with me
I'm levitating
Related Songs
Carolina
Taylor Swift
Levitating (Remix)
Dua Lipa
BREAK MY SOUL
Beyoncé
[Post-Chorus]
You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
Yeah, yeah, yeah, yeah, yeah
I'm levitating (Woo)
You can fly away with me tonight
You can fly away with me tonight
Baby, let me take you for a ride
Yeah, yeah, yeah, yeah, yeah (Woo)

[Bridge]
My love is like a rocket, watch it blast off
And I'm feeling so electric, dance my ass off
And even if I wanted to, I can't stop
Yeah, yeah, yeah, yeah, yeah
My love is like a rocket, watch it blast off
And I'm feeling so electric, dance my ass off
And even if I wanted to, I can't stop
Yeah, yeah, yeah, yeah, yeah

[Pre-Chorus]
You want me, I want you, baby
My sugarboo, I'm levitating
The Milky Way, we're renegading
[Chorus]
I got you (Yeah), moonlight, you're my starlight
I need you all night (All night), come on, dance with me
I'm levitating (Woo)"""

print(text)
print(len(text))
print(text.split())
print(len(text.split()))

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1



print(word_count)
