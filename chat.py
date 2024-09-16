import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason
import vertexai.preview.generative_models as generative_models

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "computing-sga-2024-03de7e1a0935.json"

def init_cs_bot_session():
  context = """
      kamu adalah seorang kostumer service dari Use Experience Questionare. kamu bertugas menjawab pertanyaan dari costumer mengenai UEQ atau Use Experience Questionare. Untuk informasi OY Indonesia bisa dilihat pada dibawah

      User Experience
Questionnaire Handbook
All you need to know to apply the UEQ
successfully in your projects
Author: Dr. Martin Schrepp
Version 11 (12.09.2023)
Introduction
The knowledge required to apply the User Experience Questionnaire (UEQ) is currently split
into several independent publications. The goal of this handbook is to bring all these pieces of
knowledge together into one document. This will make it hopefully easier for practitioners to
apply the UEQ in their evaluation projects.
We focus on the most important facts to keep the document short (since each additional page
will reduce the number of people who read it significantly). We cite some publications for
those who want to dig deeper into the subject. Please check in addition to this handbook the
web site www.ueq-online.org for new developments and publications concerning the UEQ.
Construction of the UEQ
The original German version of the UEQ was created in 2005. A data analytical approach was
used in order to ensure a practical relevance of the constructed scales, i.e. the scales were
derived from data concerning a bigger pool of items. Each scale describes a distinct quality
aspect of an interactive product.
In brainstorming sessions with usability experts, an initial item set of 229 potential items
related to user experience was created. This item set was then reduced to an 80 items raw
version of the questionnaire by an expert evaluation.
In several studies focusing on the quality of interactive products, including e.g. a statistics
software package, cell phone address books, online-collaboration software or business
software, data were collected with this 80 item raw version. In total 153 participants answered
the 80 items of the raw version. Finally, the 6 UEQ scales and the items representing each
scale were extracted from this data set by principal component analysis.
The items have the form of a semantic differential, i.e. each item is represented by two terms
with opposite meanings. The order of the terms is randomized per item, i.e. half of the items
of a scale start with the positive term and the other half of the items start with the negative



2
term. We use a seven-stage scale to reduce the well-known central tendency bias for such
types of items.
An example of an item is:
attractive o o o o o o o unattractive
The items are scaled from -3 to +3. Thus, -3 represents the most negative answer, 0 a neutral
answer, and +3 the most positive answer.
The consistency of the UEQ scales and their validity (i.e. the scales really measure what they
intend to measure) was investigated in 11 usability tests with a total number of 144
participants and in an online survey with 722 participants. The results of these studies showed
a sufficiently high scale consistency (measured by Cronbach’s Alpha). In addition, a number of
studies showed a good construct validity of the scales.
If you want to know more details about construction and validation of the UEQ, see:
Laugwitz, B., Schrepp, M. & Held, T. (2008). Construction and evaluation of a user experience
questionnaire. In: Holzinger, A. (Ed.): USAB 2008, LNCS 5298, 63-76.
Scale structure
The UEQ contains 6 scales with 26 items:
• Attractiveness: Overall impression of the product. Do users like or dislike the
product?
• Perspicuity: Is it easy to get familiar with the product? Is it easy to learn how to
use the product?
• Efficiency: Can users solve their tasks without unnecessary effort?
• Dependability: Does the user feel in control of the interaction?
• Stimulation: Is it exciting and motivating to use the product?
• Novelty: Is the product innovative and creative? Does the product catch the
interest of users?
Attractiveness is a pure valence dimension. Perspicuity, Efficiency and Dependability are
pragmatic quality aspects (goal-directed), while Stimulation and Novelty are hedonic quality
aspects (not goal-directed).
The Attractivenessscale has 6 items, all other scales have 4 items. Figure 1 shows the assumed
scale structure of the UEQ and the English items per scale.
3
Figure 1: Assumed scale structure of the UEQ.
Typical application scenarios
A number of different research questions can be answered by a quantitative measurement of
a products user experience with the UEQ.
Compare the user experience of two products
A typical scenario is to compare an established product version with a redesigned version to
check if the new version has better user experience. Another scenario is to compare a product
to direct competitors in the market.
Products can be compared relatively easy by a statistical comparison of two UEQ
measurements. Thus, the UEQ evaluations of both products or both product versions are
compared on the basis of the scale means for each UEQ scale.
Let’s look at an example. Figure 2 shows a comparison of two hypothetical product versions A
(new) and B (old).
4
Figure 2: Comparison of two hypothetical product versions.
As we can see, the new version A shows for all scales, with the exception of Novelty where the
values are approximately the same, better values than the old version B. However, if you want
to draw conclusions on this result (especially if your sample is small) you have to check if the
differences are significant.
The error bars represent the 95% confidence intervals of the scale mean. What do they mean?
Assume you could repeat an evaluation infinitely often under the same conditions. Then of
course due to some random influences you would not measure the exactly same scale mean
in each repetition. The 95% confidence interval is the interval in which 95% of the scale means
of these hypothetical repetitions are located. Thus, it shows how accurate your measurement
is.
If the confidence intervals of the two measurements do not overlap, then the difference is
significant on the 5% level. In our example above this is only true for the scale Efficiency. But
the opposite conclusion is not true, i.e. if the confidence intervals overlap the differences can
still be significant. Thus, it makes sense to do a significance test (a simple two sample t-test
assuming unequal variances can be done with the Excel
UEQ_Compare_Products_Version<x>.xlsx (<x> is the version number that change with each
new version of the Excel) available for download on www.ueq-online.org or can easily be done
with each statistics package).
If you compare a new version with an already used version, you should try to collect the data
after the users have made themselves familiar with the new version. If you start data
collection directly after the new version is launched, problems occurring from the change itself
(i.e. things work in the new version differently than in the old version and users are irritated
or angry about that, even if the new version is better) may influence your results heavily.

-1,5
-1
-0,5
0
0,5
1
1,5
Version A
Version B
5
Test if a product has sufficient user experience
Does the product fulfil the general expectations concerning user experience? Such
expectations of users are formed by products they frequently use.
Sometimes the answer to this question is immediately clear given the scale means, as in the
following example:
Figure 3: Example of a product with good results.
Here obviously, all scales show an extremely positive evaluation. The standard interpretation
of the scale means is that values between -0.8 and 0.8 represent a neural evaluation of the
corresponding scale, values > 0,8 represent a positive evaluation and values < -0,8 represent
a negative evaluation.
The range of the scales is between -3 (horribly bad) and +3 (extremely good). But in real
applications in general only values in a restricted range will be observed. Due to the calculation
of means over a range of different persons with different opinions and answer tendencies (for
example the avoidance of extreme answer categories) it is extremely unlikely to observe
values above +2 or below -2.
But in typical evaluations things are not so obvious. To get a better picture on the quality of a
product it is thus necessary to compare the measured user experience of the product to
results of other established products, for example from a benchmark data set containing quite
different typical products.
The UEQ offers such a benchmark, which contains in the moment the data of 452 product
evaluations with the UEQ (with a total of 20190 participants in all evaluations). The benchmark
is updated once a year, so make sure that you always download the latest version of the ExcelTool from the web-site www.ueq-online.org.
-3
-2
-1
0
1
2
3
6
The benchmark classifies a product into 5 categories (per scale):
• Excellent: In the range of the 10% best results.
• Good: 10% of the results in the benchmark data set are better and 75% of the
results are worse.
• Above average: 25% of the results in the benchmark are better than the result
for the evaluated product, 50% of the results are worse.
• Below average: 50% of the results in the benchmark are better than the result
for the evaluated product, 25% of the results are worse.
• Bad: In the range of the 25% worst results.
The benchmark graph from the Excel-Tool shows how the UX quality of your evaluated
product is.
Figure 4: Benchmark graph for a hypothetical product.
Determine areas of improvement
What should be changed in order to improve the user experience of the product? This
question cannot be answered directly by a quantitative measurement of user experience. To
answer this question, a connection of product features to the measurement is required.
However, with a questionnaire like the UEQ it is possible to make at least educated guesses
about the areas where improvements will have the highest impact. For an evaluated product,
the UEQ shows a pattern of 6 measured user experience qualities. From this pattern it is
possible to make at least some assumptions where to look for improvements.
More details about the application scenarios of the UEQ and some examples are contained in:
Schrepp, M.; Hinderks, A. & Thomaschewski, J. (2014). Applying the User Experience Questionnaire (UEQ) in
Different Evaluation Scenarios. In: Marcus, A. (Ed.): Design, User Experience, and Usability. Theories, Methods,
and Tools for Designing the User Experience. Lecture Notes in Computer Science, Volume 8517, 383-392, Springer
International Publishing.
-1,00
-0,50
0,00
0,50
1,00
1,50
2,00
2,50
Excellent
Good
Above Average
Below Average
Bad
Mean
7
Details about the creation of the benchmark can be found in:
Schrepp, M.; Hinderks, A. & Thomaschewski, J. (2017). Construction of a benchmark for the User Experience
Questionnaire (UEQ). International Journal of Interactive Multimedia and Artificial Intelligence, Vol. 4(4), 40-44.
Translation to other languages
The UEQ is already translated into a number of languages (21 at the point in time of the last
update of this handbook). The complete and actual list of all available language versions can
be found on www.ueq-online.org. If there is no version available for your language, then
simply create one!
The following process was used in nearly all current translations and usually helps to get a
good result out of the translation process.
1. Choose one of the existing language versions as a basis for the translation. We
call the language of this version in the following the source language.
2. Translate the instructions and the terms of the items into your language (target
language). Remember that each item consists of two terms that represent the
opposites of a semantic dimension. Make sure that this is also true after the
translation.
3. Find somebody else who translates the items of the target language back to
the source language. It is important that the translation into the target
language and the translation back are done by two independent persons.
4. Analyse the deviations between the UEQ version you based the translation on
and the version that result from translation back into the source language.
5. If possible, collect some data (preferably from several products) with the new
translation and check if the Cronbach alpha values are sufficiently high. If this
is not possible publish your translation on www.ueq-online.org, others may use
it and contribute their data.
6. Do not forget to send us your translation! We will publish it with your name (if
you agree, publication without author name is also possible) as author on the
UEQ website. Even if it is not perfect, that is a good start and others may use it
and share their data, which can then be used to improve the language version.
More details about the translation process and methods to check the quality of the language
version are given in:
Rauschenberger, M., Schrepp, M., Cota, M.P., Olschner, S. & Thomaschewski, J. (2013). Efficient measurement of
the user experience of interactive products - How to use the User Experence Questionnaire (UEQ). Example:
Spanish Language Version. International Journal of Interactive Multimedia and Artificial Intelligence, Vol. 2(1),
39- 45.
Online application
The UEQ is short enough to be applied online. This saves a lot of effort in collecting the data.
However, please consider that in online studies you may have a higher percentage of persons
who do not fill out the questions seriously. This is especially true if the participants get a
reward (for example participation in a lottery) for filling out the questionnaire.
8
A simple strategy to filter out suspicious responses is based on the fact that all items in a scale
more or less measure the same quality aspect. Thus, the responses to these items should be
at least not too different.
As an example, look at the following responses to the items of the scale Perspicuity:
not understandable o o o o o x o understandable
easy to learn o o o o o o x difficult to learn
complicated o o o o x o o easy
clear o o o o o x o confusing
Obviously, these answers are not very consistent. If they are transferred to the order negative
(1) to positive (7), then we can see that the ratings vary from 1 to 6, i.e. the distance between
the best and worst answer is 5. Thus, a high distance between the best and the worst answer
to all items in a scale is an indicator for an inconsistent or random answer behaviour.
If such a high distance occurs only for a single scale this is not really a reason to exclude the
answers of a participant, since such situations can also result from response errors or a simple
misunderstanding of a single item. If this occurs for several scales, then it is likely that the
participant has answered at least a part of the questionnaire not seriously.
Thus, a simple heuristic is to consider a response as suspicious if for 2 or 3 scales (it is open to
your decision how strict you will apply this rule) the distance between best and worst response
to an item in the scale exceeds 3.
This heuristic is enhanced with a second heuristic that uses the number of identical answers
by a participant. If, for example, a participant crosses for all 26 items the middle answer
category, this clearly indicates that not much thinking was spent to answer the questionnaire.
An analysis of several data sets indicates that responses that contain more than 15 identical
answer categories (for the 26 items) should be removed before the data are analysed.
These heuristics are also implemented in the Excel-Tools for the UEQ and the short version of
the UEQ (described below) in one of the worksheets. Details on how these heuristics were
derived and empirically evaluated can be found in:
Schrepp, M. (2016). Datenqualität bei Online-Fragebögen sicherstellen. S. Hess & H. Fischer (Eds.): Mensch und
Computer 2016 – Usability Professionals. http://dx.doi.org/10.18420/muc2016-up-0015.
Schrepp, M. (2023). Enhancing the UEQ heuristic for data cleansing by a threshold for the number of identical
responses. Research report, DOI: 10.13140/RG.2.2.35853.00480.
Applying the UEQ as part of a Usability Test
Often the UEQ is used as part of a classical usability test to collect some quantitative data
about the impression of the participants concerning user experience. The best point in time
to hand over the questionnaire to the participants is directly after they finished working on
the test tasks. If participants fill the questionnaire after they had a lengthy discussion about
the product with the person conducting the test, this will influence the results. The goal of the
UEQ is to catch the immediate impression of a user towards a product. Thus, try to get the
answers to the UEQ before you discuss with the participants.
9
Some of the participants may be unfamiliar with the special item format of the questionnaire.
Mention that this is a scientifically evaluated questionnaire to measure user experience when
you hand it over to the participant. This will improve the quality and consistency of the
answers.
How to use the Excel-Tool?
The goal of the Excel-Tool is to make the analysis of UEQ data as easy as possible for you. You
just need to enter the data in the corresponding work sheet in the Excel
UEQ_Data_Analysis_Tool_Version<x>.xlsx and then all relevant computations (with the
exception of significance tests if you want to compare two products, here you need to use the
Excel UEQ_Compare_Products_Version<x>.xlsx) are done automatically.
The Excel-Tool contains comments that explain the different calculations, thus we need not to
go into details here. Make sure that you always use the most actual version of the Excel-Tool
that is available on www.ueq-online.org, since the UEQ team tries to continuously improve
this tool based on user feedback.
How to interpret the data
What do the error bars mean?
The error bar of a scale shows the 95% confidence interval of the scale mean. The error bars
are displayed together with the scale means in the corresponding diagram of the Excel-Tool.
Assume you could repeat an evaluation often under the same conditions. Then of course due
to some random influences you would not measure the same scale mean in each repetition.
The error bar describes the interval in which 95% of the scale means of these repetitions will
be located. Thus, it shows how accurate your measurement is. The size of the error bar
depends on the sample size (the more participants you have, the smaller is typically the error
bar) and on how much the different participants agree (the higher the level of agreement, i.e.
the more similar the answers are, the smaller is the error bar).
Thus, if the confidence interval is relatively large you should interpret your results carefully.
In this case your measurement may not be very accurate. Typically, this is due to a too small
sample size, i.e. if possible you should collect some more data. The Excel-Tool contains a tab
Sample_Size that helps you to estimate how many data you need to collect to reach a given
precision in the estimation of the scale means.
How many data do I need?
As described above, the error bars (the 95% confidence intervals) for the scale mean, describe
how accurate or exact the measured scale mean is. A natural question in planning a new study
based on a UEQ survey is therefore how many participants are required to reach a given width
of the confidence interval. Together with the data analysis tools a special Excel
(Sample_size_estimator.xlsx) can be downloaded that assists you in planning the required
sample size. This Excel is based on some research concerning typical standard deviations for
UEQ scales that is described in a report published on ResearchGate. This report describes also
some heuristics that should help to decide on a reasonable width of the confidence interval
for your research.
10
Schrepp, M. (2023). An analysis of standard deviations for UEQ scales. Research report published on
Researchgate, DOI 10.13140/RG.2.2.34969.08809.
Interpretation of the standard deviation
The standard deviation of a scale mean can be interpreted as a measure for the level of
agreement of the participants concerning the UX quality aspect measured by a scale. The
lower the standard deviation is, the more do different participants agree in their evaluation.
A recommendation to interpret the standard deviations of UEQ scales was derived from the
analysis of a large sample of UEQ studies. Three thresholds were defined:
• High agreement: Standard deviation of scale below 0.83.
• Medium agreement: Standard deviation of scale between 0.83 and 1.01.
• Low agreement: Standard deviation of scale above 1.01.
The basis for these thresholds is described in the research report mentioned directly above
this section.
What does the Cronbach-Alpha values mean?
One of the worksheets in the Excel-Tool shows the Cronbach-Alpha coefficients ( = 𝑛 ∗ 𝑟/1 +
(𝑛 − 1) ∗ 𝑟, where r is the mean correlation of the items in a scale and n is the number of
items in a scale) for the six scales of the UEQ. The Alpha-Coefficient is a measure for the
consistency of a scale, i.e. it indicates that all items in a scale measure a similar construct.
There are no clear rules that describe how big the Alpha-Coefficient should be. Some rules of
thumb consider values >0.6 or >0.7 as a sufficient level. If the Alpha-Value of one of the scales
is too small, then you should interpret this scale carefully.
There are two main reasons for small Alpha-values. First, a higher number of participants may
misinterpret some items in the scale. For example, the item unsecure / secure is associated
with the scale Dependability. It usually is interpreted in the sense that the interaction is save
and controllable by the user. In the context of social networks this item can be misinterpreted
as “Are my data secure?”, i.e. the item gets a non-intended meaning in this context. This
lowers the correlations to the other items in the scale and therefore the Alpha-value. Second,
a scale can be irrelevant for a certain product. In this case the answers of the persons will be
not very consistent, since participants will have problems to judge a UX quality aspect that is
for the product under investigation not important. This can also lead to low Alpha-Values. It is
clear from these examples that in such cases the scale mean should be interpreted with care.
Please note that the Alpha-Coefficient is quite sensitive to sampling effects. Thus, if you have
only a small sample (for example between 20 and 40 participants) a low Alpha value can be
the result of a sampling effect and may not necessarily indicate a problem with scale
consistency. In such cases better ignore Alpha and check directly (see below) the means of the
single items inside the scales to draw conclusions on items that are potentially critical, i.e.
misinterpreted by the participants of your study.
If the Alpha-value for a scale is small, it makes sense to look at the means of the single items.
There you can sometimes directly see if some item is not interpreted in the usual way. The
next figure shows such a case as an example.
11
Figure 5: Typical example of an item that is misinterpreted in the given context.
This example shows the result of an application of the UEQ in the context of a social network.
It is obvious that the item 17 (not secure / secure) has a negative mean, while all other items
of this scale (black bars) have a highly positive mean. This shows that there is maybe a problem
with this item in this context.
More information concerning Alpha and the effect of the sample size can be found in:
Schrepp, M. & Rummel, B., (2018). UX Fragebögen: Verwenden wir die richtigen Methoden?. In: Dachselt, R. &
Weber, G. (Hrsg.), Mensch und Computer 2018 - Workshopband. Bonn: Gesellschaft für Informatik e.V. DOI:
10.18420/muc2018-ws16-0325.
Schrepp, M. (2020). On the usage of Cronbach’s Alpha to measure reliability of UX scales. Journal of Usability
Studies, Vol. 15, Issue 4.
Short version for special application scenarios
Usually, 3-5 minutes are sufficient to fill out the UEQ including some demographic data. Thus,
the UEQ is already a quite efficient method to capture the opinion of a user towards a products
user experience. Thus, a natural question is why an even shorter version is needed at all?
-3 -2 -1 0 1 2 3
annoying/enjoyable
not understandable/understandable
dull/creative
difficult to learn/easy to learn
inferior/valuable
boring/exciting
not interesting/interesting
unpredictable/predictable
slow/fast
conventional/inventive
obstructive/supportive
bad/good
complicated/easy
unlikable/pleasing
usual/leading edge
unpleasant/pleasant
not secure/secure
motivating/demotivating
does not meet expectations/meets expectations
inefficient/efficient
confusing/clear
impractical/practical
cluttered/organized
unattractive/attractive
unfriendly/friendly
conservative/innovative
Mean value per Item
12
We received in the last couple of years several requests for such a shorter version and some
users even created their own short version by removing some items (which is not a
recommended practice). Thus, in practical applications there seems to be some use cases,
where a full UEQ is too time consuming.
All these requests came from three different generic application scenarios in which only a very
small number of items can be used to measure user experience:
1. The first scenario is collecting data when the user leaves a web shop or web
service. For example, the user just ordered something in a web shop and logs
out. After pressing the log out button the user is asked to fill out a short
questionnaire concerning the user experience of the shop. In such scenarios, it
is crucial that the user has the impression that filling out the questionnaire can
be done extremely fast. Showing a full UEQ with all 26 questions will restrict
the number of users willing to give feedback massively.
2. In the second scenario a questionnaire concerning user experience should be
included in an already existing product experience questionnaire. Typically,
such a questionnaire is sent out after a customer has purchased a product and
already used it for some time. Such questionnaires try to collect data about the
complete product experience, for example why the customer had chosen the
product, if the functionality of the product fulfils the expectations, etc. Thus,
such questionnaires tend to be quite lengthy and thus it is difficult to add a full
26 item user experience questionnaire.
3. A third scenario sometimes mentioned are experimental settings where a
participant needs to judge the user experience of several products or several
variants of a product in one session. In such scenarios, the products or product
variants are presented in random order one after the other to the participant,
who must fill out a questionnaire concerning user experience for each of them.
In such a setting, the number of items must be kept to a minimum. Otherwise
the participant will be stressed and the quality of the answers will suffer.
To fulfil these requirements a short version of the UEQ was constructed that consists of just 8
items. 4 of these items represent pragmatic quality (items 11, 13, 20 and 21 of the full UEQ)
and 4 hedonic quality aspects (items 6, 7, 10 and 15 of the full UEQ). Thus, the short version
does not provide a measurement on all UEQ scales. It consists of the scales Pragmatic Quality
and Hedonic Quality. In addition, an overall scale (mean of all 8 items) is reported.
You should be careful to interpret the overall scale. It cannot be interpreted easily as an overall
KPI for user experience. The reason is that the importance of the pragmatic respectively
hedonic quality for the users may not be the same for the evaluated product. Pragmatic
quality may be more important than hedonic quality for some products, while the opposite
may be true true for other products. Thus, interpret the overall value with care.
Since the items of the short version are just a subset of the full version, the short version is
available in all languages for which a translation of the full UEQ is available.
To allow a fast processing of the items the negative term of an item is always left and the
positive always right. First the pragmatic items are shown followed by the hedonic items.
13
The English version of the short UEQ looks like this:
obstructive o o o o o o o supportive
complicated o o o o o o o easy
inefficient o o o o o o o efficient
confusing o o o o o o o clear
boring o o o o o o o exciting
not interesting o o o o o o o interesting
conventional o o o o o o o inventive
usual o o o o o o o leading edge
The materials of the short version of the UEQ can be downloaded in a separate package from
www.ueq-online.org. This package contains a document with the items for all languages and
an Excel-Tool for data analysis. Since the use cases for which the short version makes sense
do not fit to a paper-pencil usage of the questionnaire, we do not provide a standard
instruction for the short version and no PDF documents per language.
The short version UEQ-S is intended only for special scenarios, which do not allow applying a
full UEQ. The UEQ-S does not allow to measure the detailed UX qualities Attractiveness,
Efficiency, Perspicuity, Dependability, Stimulation and Novelty, which are part of the UEQ
reporting. To get these detailed values can be quite useful in interpreting the results and
define areas of improvement.
Thus, the short version UEQ-S allows only a rough measurement on higher level metadimensions. Our recommendation is therefore to use the short version UEQ-S only in the
scenarios described above. The short version should not replace the usage of the full version
in the standard scenarios, for example after usability tests. In such scenarios the small gain in
efficiency does not compensate for the loss of detailed information about the single quality
aspects.
Details of the construction of the short version can be found in:
Schrepp, Martin; Hinderks, Andreas; Thomaschewski, Jörg (2017): Design and Evaluation of a Short
Version of the User Experience Questionnaire (UEQ-S). In: IJIMAI 4 (6), 103–108. DOI:
10.9781/ijimai.2017.09.001.
The KPI Extension
Managers love KPI’s. They reduce complex constructs to a single numerical value and thus give
the impression that things can be controlled and improved by measuring and optimizing this
single KPI. However, for a construct like UX that combines a high number of quite distinct
quality aspects, this is not easily possible.
The UEQ gives back 6 scale values that can be interpreted. It is from the design of the
questionnaire not possible to combine these into a single KPI. What can maybe theoretically
be justified is to compute a value for Pragmatic Quality from the three scales Efficiency,
Perspicuity and Dependability and a value for Hedonic Quality from Stimulation and Novelty.
14
To compute a single UX KPI from the UEQ results requires knowledge about the relative
importance of the UEQ scales to the overall impression concerning UX. One method to do this
is to add some questions that describe the content of the 6 scales in plain language and to ask
the participants how important these scales are for their impression on UX. These ratings
about the importance can then be combined with the scale means to compute the desired UX
KPI. How important a quality aspect is for the overall UX impression does obviously depend
on the concrete product evaluated. Thus, it is not possible to provide any general data about
importance of scales.
If you want to compute a meaningful KPI from the scales, then add the following 6 additional
questions to the UEQ:
• Attractiveness: The product looks attractive, enjoyable, friendly and
pleasant.
• Efficiency: I can perform my tasks with the product fast, efficient and in a
pragmatic way. The user interface looks organized.
• Perspicuity: The product is easy to understand, clear, simple, and easy to
learn.
• Dependability: The interaction with the product is predictable, secure and
meets my expectations. The product supports me in performing my tasks.
• Stimulation: Using the product is interesting, exciting and motivating.
• Novelty: The product is innovative, inventive and creatively designed.
These questions could be rated on a 7-point Likert scale with the endpoints Not important at
all (1) and Very important (7). The additional questions should be placed behind the 26 UEQ
items. By repeating the most important positive terms the connection between the additional
question and the corresponding UEQ scale is established.
The data analysis tool contains an additional worksheet KPI_Calculation. Enter the observed
values for the 6 additional questions concerning the importance of the scales in this
worksheet. The KPI is then automatically calculated.
The additional 6 questions will be available for download in the section Questionnaires (PDF)
of the UEQ page (www.ueq-online.org). Please note that they are currently not available in all
of the language versions of the UEQ.
Details concerning this method can be found in:
Hinderks, A., Schrepp, M., Domínguez Mayo, F.J., Escalona, M.J., Thomaschewski, J. (2019).
Developing a UX KPI based on the User Experience Questionnaire. Computer Standards &
Interfaces. https://doi.org/10.1016/j.csi.2019.01.007.
Typical questions
Can I change some items?
You should NOT change single items or leave out some items in a scale! If you do this it is very
difficult to interpret your results, for example the benchmark values that are calculated based
on the original items should not be used, simply because the answers are not comparable.
15
Do I need all scales?
You can leave out complete scales, i.e. delete all items of a certain scale from the
questionnaire. This can make sense to shorten the questionnaire in cases where it is clear that
a certain scale is not of interest.
How long do participants need to fill out the questionnaire?
Applying the UEQ does not require much effort. Usually 3-5 minutes are sufficient for a
participant to read the instruction and to complete the questionnaire.
How many data do I need?
The more data you have collected, the better and more stable will be the scale means and
thus the more accurate will be the conclusions you draw from these data. However, it is not
possible to give a minimum number of data you need to collect to get reliable results. How
many data you need does depend also on the level of agreement of the users that participate
in the questionnaire (the standard deviation per scale). The more they agree, i.e. the lower
the standard deviation of the answers to the items is, the less data you need for reliable
results. For typical products evaluated so far around 20-30 persons already give quite stable
results.
The Excel-Tool for data analysis contains a worksheet named Sample_Size. Here the standard
deviation per scale is used to estimate how many data you need to reach a certain precision
(measured by the width of the confidence interval) in your measurement. Obviously, the
precision depends on the conclusions you want to draw from the data. For typical product
evaluations a precision of 0.5 seems to be adequate (see the detailed explanations in the
worksheet). A more comfortable tool is the new Sample_size_estimator.xlsx that can be
downloaded together with the data analysis tool.
How to sell it to customers and management?
If you report to your management or other stakeholders, it is important to communicate the
meaning of the UEQ scales. If you evaluate a financial software or another business tool it may
look strange to your stakeholders if you report on Stimulation or Originality. Do they want an
original accounting system? Probably not.
If necessary, change the scale names and explain clearly what each scale means. In the
example above, you may want to change Stimulation to Fun of use and Originality into Interest.
Use terms that fit the language of your stakeholders. Important is the semantic meaning of
the scales, i.e. if you change a scale name make sure the new name still covers the meaning
of the scale.
Are there benchmarks for special product types available?
The benchmark allows to compare your result to the results of other products. However, the
benchmark data set contains products of quite different types. Thus, it is often asked if there
are special benchmark data sets available that contain only products of a given type.
Due to the nature of the UEQ benchmark it is obvious that a certain number of studies is
required to create a meaningful benchmark. We can provide in the moment only two
specialised benchmarks for special product types, which are business software and web pages
16
and web services. The borders for these benchmarks and the general benchmark are shown
below.
General Benchmark (468 product evaluations)
Category Attractiveness Perspicuity Efficiency Dependability Stimulation Originality
Excellent 1.84 2.00 1.88 1.70 1.70 1.60
Good 1.58 1.73 1.50 1.48 1.35 1.12
Above average 1.18 1.20 1.05 1.14 1.00 0.70
Below average 0.69 0.72 0.60 0.78 0.50 0.16
Business Software (158 product evaluations)
Category Attractiveness Perspicuity Efficiency Dependability Stimulation Originality
Excellent 1.72 1.85 1.70 1.61 1.53 1.49
Good 1.50 1.48 1.38 1.37 1.34 1.03
Above average 1.11 1.03 0.89 1.04 1.04 0.64
Below average 0.70 0.58 0.51 0.71 0.71 0.24
Web Sites and Web Services (85 product evaluations)
Category Attractiveness Perspicuity Efficiency Dependability Stimulation Originality
Excellent 1.75 2.07 1.70 1.70 1.56 1.12
Good 1.41 1.84 1.43 1.53 1.10 0.87
Above average 0.96 1.14 0.98 1.19 0.69 0.49
Below average 0.44 0.65 0.50 0.81 0.07 -0.22
The value in a cell means that a product must exceed this value to be in the corresponding
category. Thus, to be rated as Excellent concerning Perspicuity a business software must
exceed the value 1.85, to be rated as Good it must be in the range of 1.48 and 1.85 and if it is
below 0.58 it is rated as Bad.

  """
  vertexai.init(project='computing-sga-2024',location='asia-southeast1')
  model = GenerativeModel(
      'gemini-1.5-flash-001',
      system_instruction=[context]
  )

  return model.start_chat()