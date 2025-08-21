from langchain.text_splitter import CharacterTextSplitter


text = """
A vampire is a mythical creature that subsists by feeding on the vital essence (generally in the form of blood) of the living. In European folklore, vampires are undead humanoid creatures that often visited loved ones and caused mischief or deaths in the neighbourhoods which they inhabited while they were alive. They wore shrouds and were often described as bloated and of ruddy or dark countenance, markedly different from today's gaunt, pale vampire which dates from the early 19th century.

Vampiric entities have been recorded in cultures around the world; the term vampire was popularized in Western Europe after reports of an 18th-century mass hysteria of a pre-existing folk belief in Southeastern and Eastern Europe that in some cases resulted in corpses being staked and people being accused of vampirism.[1] Local variants in Southeastern Europe were also known by different names, such as shtriga in Albania, vrykolakas in Greece and strigoi in Romania, cognate to Italian strega, meaning 'witch'.
"""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
     separator = ''
)

result = splitter.split_text(text)

print(result)