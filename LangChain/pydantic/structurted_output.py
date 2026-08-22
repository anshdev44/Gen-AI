from pydantic import BaseModel, Field
from typing import Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=1.0,
    max_tokens=None,
)


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="A list of the main themes discussed in the review."
    )

    summary: str = Field(
        description="A brief summary of what the review says."
    )

    sentiment: Literal["pos", "neg", "neutral"] = Field(
        description="The overall sentiment of the review: positive, negative, or neutral."
    )

    pros: Optional[list[str]] = Field(
        default=None,
        description="A list of positive aspects or advantages mentioned in the review."
    )

    cons: Optional[list[str]] = Field(
        default=None,
        description="A list of negative aspects or disadvantages mentioned in the review."
    )

    name: Optional[str] = Field(
        default=None,
        description="The name of the person who wrote the review, if available."
    )


review = """
I've been using the Nova X Pro for nearly six months, and my experience has been surprisingly mixed.
On the positive side, the build quality is excellent. The aluminum frame feels premium, the hinge is sturdy,
and despite carrying it around every day, I haven't noticed any creaking or noticeable wear.

The 16-inch OLED display is probably the best part of the laptop. Colors are vibrant, blacks are genuinely deep,
and the 120Hz refresh rate makes scrolling and gaming feel extremely smooth. It's also bright enough for most
indoor environments, although reflections can become distracting near windows.

Performance is another strong point. The Ryzen 9 processor handles compiling large projects, running multiple
Docker containers, and switching between several development environments without much trouble. The dedicated
GPU is capable of running modern games at 1080p with high settings, although demanding titles require some
compromises if you want consistently high frame rates.

Thermals are generally acceptable during normal workloads, but under sustained gaming or rendering loads,
the fans become quite loud and the keyboard deck gets noticeably warm.

Battery life, however, is where things become complicated. During light browsing and document editing, I can
get around seven hours, which is reasonable for a machine this powerful. But once I start using the GPU,
battery life drops dramatically. The included charger is also quite large, so this isn't exactly a laptop
I would describe as convenient for frequent travel.

The keyboard is comfortable for long programming sessions, and the trackpad is accurate, but the port selection
feels outdated. There are plenty of USB ports, but I would have preferred another USB-C port with full charging
and display support.

The speakers are another disappointment. They are clear enough for video calls and casual YouTube watching,
but they lack bass and sound noticeably thin compared with similarly priced laptops.

Software has also been a mixed experience. Most drivers have been stable, but I encountered occasional
Bluetooth disconnects and one particularly annoying issue where the laptop would randomly wake from sleep.
Firmware updates eventually improved the situation, although it took several weeks before I found a reliable fix.

Customer support was responsive when I contacted them, but their first few suggestions were generic troubleshooting
steps that I had already tried.

At $1,699, I don't think this laptop is a bad purchase, but I do think the price makes its weaknesses harder
to ignore. If you prioritize display quality, development performance, and gaming capability, it's an excellent
machine. If portability, battery life, speakers, or a completely trouble-free software experience are your
priorities, there are better alternatives.

Overall, I'd rate it around 8 out of 10, but I would recommend buying it during a sale rather than paying
the full launch price.
"""


structured_output = chat_model.with_structured_output(Review)

result = structured_output.invoke(review)

print(result)