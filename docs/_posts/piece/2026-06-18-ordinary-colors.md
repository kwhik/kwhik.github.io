---
layout: post
title:  "Ordinary Colors"
date:   2026-06-18 07:00:00 -0700
author: Mark Fussell
category: piece 
---

There are a lot of sizes to track when designing and building both the electrical and the physical aspects of solar systems.  These include sizes of:
   * **Wires:** 10AWG, 6mm², etc. 
   * **Bolts:** #6, 1/8-inch, 3mm, etc.
   * **Pipes:** 3/4-inch nominal, various outside dimensions depending on materials, etc.
   * **Holes:** Assorted sizes to accommodate outside, clearance, and tolerance dimensions for the above bolts, pipes, etc.
   * And so on...

Dealing with the various sizes in diagrams, charts, and especially with physical tools (e.g. drill bits, crimping dies, etc.) can be mentally taxing, especially if a number of the cuts _are really close_ in size and irreversible (or not easily accommodated).  This precision issue combined with tasks getting interrupted or paused makes it handy to have some mental support for determining the sizes you are working with or looking for.

Over time, I leveraged some previous systematic color work with the physical reality of "what colors are available" to come up with an effective labeling system using colors that includes:
* A dozen colors that can be put into the real world easily, with 
* Several dozen that can be used for more refined variations when needed.

The following describes that system as it exists at this point.

## The Core Concept

### An ordinal system for colors

The simplest explanation of the color system is to show the basic dozen as a table:

<img src="/images/posts/piece/2026-06-18-ordinary-colors/ColorScheme_mlf20260614e_cs_v12.png" width="240" alt="Basic Dozen Colors" />

The code for a color comes from its first and last character, which both reduces collisions (Blue and Black, Green and Grey) and avoids some spelling differences (Gray and Grey).  These dozen colors are available as electrical tape, which is made of PVC so is UV and water resistant, and can be used in the physical world very easily.  


##### Color Labeled Boxes
<img src="/images/posts/piece/2026-06-18-ordinary-colors/IMG_9090.png" width="480" alt="Color Labeled Boxes" />

##### Color Labeled Hole Saws

<img src="/images/posts/piece/2026-06-18-ordinary-colors/IMG_9093.png" width="240" alt="Color Labeled Hole Saws" />

Beyond the physical world, there are fewer constraints on the set of colors available but the core property of the system 'a color is first a name with a unique code' is maintained there as well.

#### Ordering

Given that the colors have a unique alphabetic code with intrinsic ordering, the colors themselves are 'perfectly' ordered.  We are leveraging  just the name, not any quality, of the color for the ordering. Further, Aqua (AA) is always going to be first color and Yellow (YW) will always be the last even within the extended multi-dozen system [[1]](#1)

These characteristics make for both a resilient and expansive labeling approach.

### Core Mapping Examples 

The following work through some core examples of color labeling

#### Color Mapping: US Fractional

<img src="/images/posts/piece/2026-06-18-ordinary-colors/ColorScheme_mlf20260614e_cs2_usf.png" width="180" alt="US Fractional" />

The US Fractional color mapping has spacing of '1/32' for the first seven colors up through '7/32' and '1/16' for the second five colors from '1/4' through '1/2'.  This is both practical in relative necessary precision at the smaller sizes and allows the fractions to repeat as an offset, where Yellow (YW) is either '1/2' (above zero) or '0' above major sizing values in half inches greater than zero.  

Looking again at the hole saws from above:

<img src="/images/posts/piece/2026-06-18-ordinary-colors/IMG_9093.png" width="240" alt="Color Labeled Hole Saws" />

You can see that the yellow, brown, purple, and red represent '0', '1/8', '1/4', and '3/8' off multiple major sizes like '1-inch' or '3-inches'.

#### Color Mapping: Metric and US Bolt Gauge

The same color system can be reused in completely unrelated ways as long as either the ordinal aspect is maintained or the ordinal is simply unimportant (e.g. labeling 'tools' as 'red' because... well... lots of Milwaukee packout boxes).  So Metric sizing and US Bolt gauge sizing _could be_ different.  Certainly the color 'red' doesn't mean the dimension is exactly '3/8' of an inch in metric.

But it would be nice if the colors were at least correlated and knowing what system you were in (USF, USG, Metric) was a subtle refinement.  At worse a mm or two of mismatch would be ideal.

<img src="/images/posts/piece/2026-06-18-ordinary-colors/ColorScheme_mlf20260614e_cs2_mm.png" width="240" alt="Metric and US Bolt" />

The US Gauges from #0 through #12 match the US Fractional values precisely.  A US bolt/screw guage number is a multiplier of '1/64' to be added to  a '2/64' base value, so by using only even gauges, #0 through #12 matches the USF units already labeled.  Beyond #12 there is no practical value of the gauge sizing.

The metric sizes are more approximately mapped to the US units.  Ultimately to keep within the constraint of twelve colors and to have a good correspondence to US units, M9 was dropped and M2.5 was added.  A couple other variations were tried but this one worked out the best, especially when cross-sections (e.g. mm²) come into consideration.  But none of the metric values are identical to the US value due to the core difference between the two systems.

For Metric, the numbers can be added as an offset like the USF values are, but when added as an offset 'BK' becomes '3mm' and the subsequent colors shift by one to make 'PK' = '9mm'.

#### Color Mapping: Wire Gauges

Wire gauges are based on circular cross-section.  The US has a few systems for labeling the size where the metric system is purely based on mm².  

There are more than a dozen commonly used wire sizes within normal solar system (and household electrical) usage, so we need to pick sizes for especially Aqua (AA) and Yellow (YW) that span an appropriate range and can then fill in other sizes with colors beyond the core dozen.

<img src="/images/posts/piece/2026-06-18-ordinary-colors/ColorScheme_mlf20260614e_cs3.png" width="240" alt="US Fractional" />

The choice of this particular mapping makes it possible to connect the two-dimensional circular cross-section to the one dimensional diameter and have approximately the same resistance (and current carrying capacity).

<img src="/images/posts/piece/2026-06-18-ordinary-colors/ColorScheme_mlf20260614e_cs3_all.png" width="360" alt="Multiple Dimensions" />

### More Complex Examples

The color mapping benefits more complex examples by making one part of the information "common knowledge".  This benefit arose with the creation of the Wire Gauge requirement chart, which has multiple gauges moving throughout it.  By having systematic ordinal colors, it can make following the wiring requirement easier, including being able to identify requirements on bulkhead posts (which are described in USF not AWG).

<img src="/images/ColorScheme_mlf20260614d_wg_3p.png" width="720" alt="Multiple Dimensions" />

It can be seen in this example that there are more colors and numeric equivalents than the basic twelve.  This will be discussed after some 

### Simple Numbering

The set of twelve numbers where Aqua (AA:0) and Yellow (YW:11) mark the ends enables easy ordinal marking of simple ordinal things.  For example the BMS sense wires for an 8S configuration can be marked from 0..8 + Power [10 values] with AA [GND/1-], BE [1+], BK [2+], BN [3+], GN [4+], GY [5+], OE [6+], PE [7+], PK [8+], and YW [Power; also located at 8+].  By having yellow be the highest sense wire (11) no matter how many are in series, it allows consistent identification across 4S..10S configurations.  Other than the yellow, the numbers are always in order and match the series terminal configuration.

This labeling with simple ordinal meaning is better than having an unrevealed meaning with color coding [SOK] or having no encoding at all [JK].

[[JK BMS sense wires in 4S configuration]]

### Non-Ordinal Labeling

Given the colors have names and a visible representation, they can be simply be used to label things without any relationship to the objects ordinal values.  For example, by simply labeling screws as 'BE' (blue) and bolts a 'PK' (pink) we can organize tool boxes containing screws and bolts with visual tags. 

<img src="/images/posts/piece/2026-06-18-ordinary-colors/ColorScheme_mlf20260618a_crib.png" width="360" alt="Box Labels" />

<img src="/images/posts/piece/2026-06-18-ordinary-colors/IMG_9090.png" width="480" alt="Color Labeled Boxes" />

A minor benefit is that screws if listed somewhere as a group come before bolts because blue (BE) is before pink.  The name of the group can change and their order is still the same.

Note that 'Wire' and 'Washers' are cheating and using a characteristic of the word 'W' as part of the color chosen for them.  But this is completely arbitrary / artistic vs. meaningful or useful.

## Extended Colors

In total, there are sixty-four (64) colors that are available in the full ordinal color system.  These are divided into the following sets:
   * G12: Group of 12 as described above
   * G16: Adds Lime [LE], Navy [NY], Silver [SR], and Teal [TL].  These colors exist in some tapes and non-ordinal color label systems but are rarer or harder to differentiate from other colors.  Of these, Lime [LE] is the most conspicuously different.
   * G32: Adds a whole new set of 16 colors, labels, and numbers.  This double the sets and in general puts a new entry (label and number) between every existing entry with Aqua and Yellow still being the bookends.
   * G64: Does the same again with 32 new entries.  Aqua and Yellow are still the bookends.

For these more expansive color systems, a number of the colors are only subtly different in hue from other colors.  As much as possible these subtly different colors are placed one or more steps apart from anything similar in appearance.  Also, some of the names are more unusual but this is less important as the colors are first identified by code (e.g. 'BD') which serves along with the visual color as a mnemonic for the full name ('burlywood').

The collection of all three new groups is shown in the following table:

<img src="/images/posts/piece/2026-06-18-ordinary-colors/ColorScheme_mlf20260618b_cs64.png" width="480" alt="Color Labeled Boxes" />

## Footnotes

* [1] <a id="1"/> It is simple to avoid adding alphabetically later colors like 'Zulu' .  
