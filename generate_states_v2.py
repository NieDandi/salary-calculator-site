states = [
"alabama","alaska","arizona","arkansas","california","colorado","connecticut",
"delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa",
"kansas","kentucky","louisiana","maine","maryland","massachusetts","michigan",
"minnesota","mississippi","missouri","montana","nebraska","nevada",
"new-hampshire","new-jersey","new-mexico","new-york","north-carolina",
"north-dakota","ohio","oklahoma","oregon","pennsylvania","rhode-island",
"south-carolina","south-dakota","tennessee","texas","utah","vermont",
"virginia","washington","west-virginia","wisconsin","wyoming"
]

base_url = "https://salary-calculator-site.vercel.app"

with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n')

    # Homepage
    f.write("<url>\n")
    f.write(f"<loc>{base_url}/</loc>\n")
    f.write("</url>\n\n")

    # Calculator page
    f.write("<url>\n")
    f.write(f"<loc>{base_url}/calculator.html</loc>\n")
    f.write("</url>\n\n")

    # State pages
    for state in states:
        f.write("<url>\n")
        f.write(f"<loc>{base_url}/{state}-salary-after-tax-calculator.html</loc>\n")
        f.write("</url>\n\n")

    f.write("</urlset>")

print("Sitemap generated successfully.")