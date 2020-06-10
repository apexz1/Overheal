"""Test the track_damage script."""
import os

python = "python3"
log_file = "tests/test_log.txt"
character = "Saintis"


def test_track_damage_raid(script_runner, tmpdir):
    path = tmpdir.strpath
    ret = script_runner.run(python, "track_damage.py", log_file, character, "-e", "1", "-v", "--path", path, "--raid")

    assert ret.success
    assert ret.stderr == ""

    assert ret.stdout == """\
0.0 0
2.996 0
3.373 -811
3.785 -510
4.989 -1162
6.617 0
7.032 -520
7.828 0
7.998 0
8.783 0
10.253 -776
11.002 -776
13.784 -475
13.995 -475
14.067 -475
15.121 -15
15.541 -15
16.741 -427
17.015 -427
17.015 -427
17.063 -427
17.545 -427
18.31 -427
18.37 -940
18.37 -15
18.37 -626
18.8 -626
19.574 -626
19.574 -626
19.574 -1460
20.011 -1460
20.07 -1460
20.381 -626
21.193 -626
21.611 -15
22.005 -698
22.408 -698
23.078 -698
23.213 -20
23.618 -20
23.619 -20
23.777 -20
24.026 -20
24.026 -20
24.026 -20
24.026 -20
24.026 -700
24.599 -700
24.849 -690
24.849 -25
24.849 -25
25.239 -992
25.656 -25
25.656 -25
26.053 -25
26.053 -25
26.075 -25
26.455 -25
26.455 -25
26.455 -25
26.615 -25
27.263 -25
27.263 -1099
27.585 -1099
27.673 -1089
27.673 -462
28.476 -25
28.476 -25
28.779 -25
28.901 -25
28.901 -25
29.509 -25
29.616 -25
29.713 -25
29.713 -25
29.713 -25
29.713 -550
29.713 -25
30.099 -25
30.135 -25
30.495 -25
30.618 -25
30.921 -25
30.921 -25
30.921 -25
30.921 -25
31.709 -25
32.122 -25
32.552 -25
32.552 -3276
32.642 -3276
33.605 -3276
33.737 -3276
33.794 -2975
33.917 -2657
34.161 -1716
34.55 -1189
34.55 -760
34.752 -760
35.608 -760
35.765 -34
36.17 -34
36.573 -796
36.573 -34
36.573 -728
36.598 -728
36.979 -728
37.798 -1202
38.598 -513
38.617 -513
38.787 -513
39.02 -1691
39.02 -513
39.151 -513
39.406 -513
39.656 -513
40.222 -513
40.222 -513
41.027 -1420
41.12 -1420
42.243 -773
43.465 -518
43.786 -518
43.875 -518
44.051 -518
44.277 -518
44.669 -518
45.093 -518
45.496 -518
45.496 -518
45.496 -518
45.496 -518
45.791 -518
46.281 -518
46.625 -518
46.695 -518
47.089 -518
47.089 -518
47.11 -518
47.676 -518
47.906 -518
48.297 -518
48.324 -518
48.718 -518
48.789 -518
49.121 -518
49.517 -518
49.517 -518
49.517 -518
49.538 -3725
49.646 -3725
49.683 -3725
50.336 -3725
50.684 -3725
50.771 -2739
51.15 -2739
51.566 -2739
51.566 -2739
51.566 -2739
51.566 -2314
51.985 -1138
52.369 -1138
52.697 -1138
52.775 -523
53.176 -1163
53.353 -1163
53.596 -1163
53.596 -1163
53.596 -1163
53.596 -523
53.687 -523
53.782 -523
53.984 -523
54.387 -523
54.387 -523
54.387 -523
54.387 -523
55.186 -523
55.186 -1316
55.698 -1316
56.005 -1918
56.364 -1918
56.673 -1918
56.811 -1918
56.811 -1918
57.216 -1918
57.216 -527
57.216 -1104
57.216 -983
57.216 -509
57.216 -986
57.394 -733
57.622 -733
57.622 -733
58.041 -530
58.452 -530
58.684 -530
58.844 -530
59.34 -530
59.652 -530
59.672 -530
60.057 -1256
60.092 -1256
60.867 -1256
60.87 -1256
61.272 -1256
61.272 -1246
61.699 -1246
62.083 -1236
62.083 -1226
62.083 -530
62.342 -530
62.487 -530
62.487 -530
62.487 -530
62.642 -530
62.888 -530
62.888 -530
62.888 -3536
63.292 -3536
63.292 -2325
63.464 -2325
63.7 -2325
64.1 -2315
64.104 -1317
64.104 -2604
64.496 -2604
64.496 -2604
64.917 -2127
65.314 -1192
65.352 -1192
65.73 -63
66.127 -63
66.309 -63
66.477 -63
66.53 -63
66.932 -63
66.958 -63
67.353 -63
67.353 -63
67.353 -63
67.745 -63
67.745 -63
67.745 -1059
67.745 -129
68.555 -129
68.557 -129
68.557 -129
68.679 -129
68.977 -850
68.979 -63
69.13 -63
69.388 -63
69.459 -63
69.776 -63
69.776 -63
70.189 -63
70.189 -63
70.591 -63
70.591 -63
70.591 -63
70.611 -683
70.745 -683
70.996 -673
71.42 -1303
71.42 -1303
71.798 -1303
71.827 -1303
72.206 -1303
72.478 -1303
72.621 -1303
72.621 -1303
73.016 -1303
73.016 -1303
73.016 -1677
73.016 -682
73.2 -682
73.832 -682
73.832 -682
73.832 -72
74.637 -72
74.637 -72
75.056 -72
75.057 -72
75.057 -72
75.057 -72
75.057 -72
75.467 -72
75.467 -72
75.467 -72
76.188 -72
76.28 -72
76.28 -72
76.67 -72
76.736 -72
77.9 -72
79.119 -72
79.119 -72
79.119 -72
79.201 -72
79.276 -72
79.51 -72
79.51 -72
80.239 -72
80.741 -72
81.116 -72
81.159 -72
81.159 -72
81.236 -72
81.562 -72
81.562 -72
81.967 -72
82.124 -72
82.199 -72
82.274 -72
82.773 -72
82.871 -72
83.167 -72
83.182 -72
84.393 -72
84.393 -72
84.393 -72
85.127 -72
85.197 -72
85.268 -72
85.606 -72
85.998 -72
86.189 -72
87.227 -72
87.611 -72
88.011 -72
88.111 -72
88.432 -72
88.829 -72
89.192 -72
89.228 -72
89.634 -72
91.106 -72
92.18 -72
92.471 -280
92.471 -280
92.471 -451
92.874 -441
92.874 -431
93.271 -643
94.1 -826
94.117 -826
94.509 -816
94.509 -806
94.509 -796
94.901 -937
95.18 -937
95.304 -917
95.304 -897
95.304 -1062
95.702 -1229
96.128 -1209
96.49 -1108
96.921 -1322
96.921 -1539
97.323 -1691
97.323 -1875
97.731 -2015
98.133 -2247
98.169 -2247
98.537 -2227
98.537 -2365
98.537 -2584
98.537 -2801
98.537 -3006
98.537 -3205
98.948 -3185
98.948 -3376
99.342 -3356
99.342 -3515
99.342 -3741
99.758 -3721
99.758 -3866
100.139 -4137
100.569 -4309
100.569 -4505
100.569 -4720
100.569 -4904
100.952 -5111
100.952 -5378
101.355 -5512
101.355 -5820
101.539 -5820
101.762 -5979
101.762 -4716
101.801 -3738
102.187 -4005
102.187 -4331
102.596 -4632
102.596 -4905
102.596 -5041
102.999 -5041
102.999 -5258
103.392 -5510
103.392 -5510
103.53 -5405
103.782 -5385
103.782 -5365
103.957 -5365
104.211 -5345
104.211 -5325
104.211 -5815
104.211 -6168
104.531 -6168
104.61 -6326
104.61 -6734
105.01 -6999
105.033 -7709
105.033 -7904
105.424 -7884
105.424 -7884
105.424 -7656
105.424 -6628
106.238 -6923
106.238 -7277
106.34 -9223
106.34 -9841
106.34 -12082
106.34 -13423
106.34 -13339
106.639 -13044
106.639 -13452
106.639 -13534
106.955 -13534
107.053 -13514
107.053 -13494
107.053 -13474
107.053 -14042
107.053 -14022
107.057 -14308
107.057 -14308
107.057 -14868
107.446 -14868
107.536 -14868
107.608 -14868
107.843 -14013
108.12 -14013
108.264 -14013
108.264 -14238
108.264 -13241
108.682 -13241
108.682 -13477
108.763 -15476
108.763 -16853
108.763 -17770
109.098 -17981
109.098 -17961
109.098 -18234
109.098 -18459
109.896 -18459
109.896 -18158
109.896 -18158
109.966 -18158
110.293 -16841
110.293 -16841
110.293 -16841
110.549 -16841
110.606 -16841
110.7 -17007
110.7 -17243
110.7 -17453
110.7 -17664
110.7 -17865
111.089 -17865
111.089 -16742
111.089 -17091
111.52 -17071
111.52 -17051
111.52 -16216
111.925 -16621
112.325 -16621
112.636 -16510
112.725 -16510
112.957 -16510
113.126 -16490
113.126 -15139
113.126 -15139
113.303 -16735
113.551 -17024
113.551 -17024
113.596 -16770
113.909 -16666
113.953 -16666
113.953 -15576
113.953 -15743
114.34 -15723
114.34 -15210
115.96 -15210
115.96 -14806
115.96 -14204
115.96 -13281
115.96 -11115
115.96 -11115
116.122 -11115
116.224 -12001
116.224 -13800
116.604 -13765
117.179 -12368
117.179 -12368
117.744 -12133
117.745 -11880
117.989 -10651
118.389 -10537
118.389 -10083
118.389 -10083
118.795 -9936
119.128 -9936
119.603 -9936
119.603 -8589
119.603 -8589
120.017 -8589
120.744 -8589
120.744 -8589
121.635 -8361
122.033 -8361
122.129 -8361
123.749 -8361
123.749 -8361
124.878 -10730
124.878 -12702
124.878 -14131
124.878 -15233
125.137 -15233
125.29 -13434
125.29 -13434
125.29 -12907
126.746 -12907
126.746 -12671
127.309 -12651
128.132 -12651
128.259 -14428
128.26 -16023
128.26 -17044
128.26 -18034
128.667 -18034
128.917 -18034
128.917 -16622
129.317 -15816
129.746 -15581
129.746 -15581
129.8 -15478
129.884 -15225
130.307 -14989
130.693 -14989
130.793 -14876
131.341 -14155
131.676 -14155
131.747 -13414
131.747 -12214
132.165 -11963
132.166 -13804
132.166 -15678
132.166 -17616
132.9 -17363
133.137 -17363
133.305 -17127
133.704 -17127
133.771 -15915
133.771 -15915
134.678 -15915
134.74 -15662
134.74 -15426
135.438 -17279
135.689 -16249
135.814 -14975
135.899 -14722
136.224 -13127
136.32 -12891
136.717 -12891
137.663 -12891
137.755 -12638
137.755 -12638
137.816 -12119
138.226 -12042
138.886 -11789
139.301 -11783
139.412 -10710
139.465 -10410
139.7 -10410
140.661 -9307
140.661 -8927
140.687 -8927
140.74 -8927
140.74 -8927
141.074 -8927
141.893 -8674
142.116 -8424
142.311 -8424
142.688 -7230
142.688 -7230
142.707 -7230
143.097 -6177
143.117 -6177
143.494 -6177
143.494 -8136
143.494 -8707
143.494 -9757
143.734 -9757
143.734 -9757
144.117 -9757
145.533 -9757
145.922 -9512
146.316 -9492
146.751 -9492
146.751 -9492
146.798 -10507
147.121 -10507
147.927 -10487
147.927 -10487
147.927 -10487
149.139 -9963
149.139 -8021
149.948 -7210
151.586 -7210
152.047 -7210
152.806 -7210
152.806 -7210
153.198 -7210
153.394 -6960
153.61 -6960
154.014 -8310
154.014 -9816
154.014 -11622
154.099 -11531
155.616 -10481
157.231 -11850
157.231 -13168
157.231 -14672
157.231 -16273
157.231 -15040
157.647 -16525
157.647 -18173
157.647 -18153
158.043 -19614
158.062 -21005
158.062 -22638
158.062 -22638
158.443 -24114
158.443 -25485
158.448 -26600
158.448 -27442
158.448 -29025
158.791 -29025
159.262 -29005
159.262 -29005
159.429 -28749
159.668 -28749
159.668 -27821
160.072 -27821
160.072 -27821
160.464 -27076
160.554 -26983
160.874 -26983
161.679 -25838
162.075 -25838
162.075 -25066
162.39 -25066
162.492 -27799
162.495 -29827
162.495 -32955
162.495 -33343
162.495 -36858
162.495 -39362
162.518 -41371
162.518 -43978
162.518 -47463
162.518 -47463
162.901 -46337
163.298 -45929
163.551 -45920
163.719 -45910
163.86 -45657
164.122 -45647
164.122 -45244
164.122 -44653
164.122 -43701
164.498 -42677
164.498 -42677
164.567 -41346
164.699 -41346
164.92 -41336
165.321 -41336
165.321 -41326
165.502 -41073
166.14 -41063
166.14 -41063
166.14 -39961
166.53 -38121
166.714 -37868
166.873 -37615
168.141 -37595
168.509 -37342
168.558 -37333
168.964 -37333
168.964 -37333
168.964 -39392
169.367 -39372
169.712 -39119
169.713 -37397
169.88 -37351
170.184 -38481
170.57 -38461
170.57 -38441
170.991 -38441
170.991 -38441
170.991 -37554
170.991 -38351
171.403 -38351
171.403 -38351
171.57 -37198
171.799 -37178
171.799 -37158
171.799 -36016
171.953 -35710
172.199 -34915
172.591 -34895
172.698 -34642
172.862 -34642
173.001 -34642
173.001 -35682
173.001 -34551
173.001 -33298
173.432 -33278
173.432 -32907
173.432 -32329
173.432 -31551
173.579 -31551
174.244 -31551
174.245 -31531
174.245 -30296
174.658 -29865
174.658 -29644
174.658 -28728
174.978 -28728
175.075 -28728
175.075 -29474
175.075 -29628
175.075 -30119
175.454 -30119
175.454 -31751
175.726 -31751
175.88 -31751
175.88 -31751
175.88 -31751
175.88 -31597
175.88 -31597
175.88 -31597
175.904 -31597
176.262 -30391
176.682 -30391
177.486 -29242
177.486 -27937
177.726 -27862
177.899 -27862
177.963 -27862
178.01 -27088
178.311 -28322
178.311 -29605
178.311 -31160
178.311 -32673
178.311 -34339
178.311 -35538
178.554 -35529
178.71 -36960
178.71 -38417
178.71 -38870
178.71 -38850
178.71 -38597
179.108 -39925
179.108 -41373
179.108 -42903
179.506 -44537
179.506 -45880
179.506 -45097
179.916 -46550
179.916 -48089
179.916 -48777
180.502 -48523
180.961 -48218
181.119 -47020
181.537 -46579
181.949 -48025
182.35 -48005
182.35 -48005
182.35 -48005
182.35 -47173
183.489 -47173
183.538 -48076
183.538 -48927
183.538 -48927
183.559 -48918
183.959 -48918
183.959 -48918
183.963 -48628
183.963 -48181
183.963 -47162
183.963 -46857
184.365 -46837
184.794 -46631
185.091 -46522
185.184 -46102
185.184 -45268
185.588 -46147
186.023 -45035
186.164 -44743
186.404 -44743
186.404 -44723
186.404 -43470
186.493 -43470
186.815 -43221
186.815 -42794
186.815 -42120
186.815 -43336
187.627 -43316
187.627 -41163
187.627 -40050
188.03 -39292
188.433 -39272
188.433 -38509
188.547 -38509
188.578 -38509
188.831 -38509
188.985 -38427
189.16 -38293
189.246 -37071
189.246 -36421
189.246 -36128
189.246 -35682
189.246 -35238
189.246 -38532
189.246 -41080
189.246 -44141
189.481 -44141
189.661 -44141
189.661 -44141
189.661 -44141
189.661 -44131
189.661 -44121
189.666 -44101
190.049 -44091
190.069 -43909
190.069 -43727
190.069 -42968
190.862 -42948
190.862 -42255
190.862 -42255
190.862 -43229
190.862 -42870
191.26 -42870
191.544 -42846
191.691 -42558
191.691 -42131
191.691 -42131
191.691 -40861
192.154 -40861
192.176 -40861
192.491 -40841
192.491 -40841
192.494 -40070
192.494 -40070
192.808 -40070
192.893 -40060
192.893 -40050
192.893 -39948
192.893 -37858
192.893 -38649
192.893 -38649
193.296 -37010
193.556 -37010
193.708 -37010
193.708 -37010
193.85 -36919
193.867 -36919
194.674 -36834
194.913 -36834
194.913 -36834
195.161 -36834
195.317 -36834
195.317 -37464
195.317 -36834
195.317 -35530
195.726 -35530
195.729 -35530
195.729 -36254
195.729 -36919
196.537 -36919
196.537 -37658
196.875 -37658
196.939 -38210
197.343 -38190
197.343 -38947
197.752 -38212
198.151 -38212
198.178 -38212
198.581 -37901
198.581 -37892
198.727 -37600
198.97 -37580
199.067 -37580
199.386 -37580
199.386 -37560
199.386 -35816
199.773 -35816
199.882 -35563
200.195 -37016
200.195 -38469
200.198 -40113
200.541 -38647
200.582 -40212
200.582 -41396
200.998 -42813
200.998 -44213
200.998 -45888
200.998 -44492
201.408 -45077
201.728 -44785
201.792 -46261
202.198 -46869
202.617 -47201
202.864 -46948
203.404 -47216
203.404 -47497
203.559 -47488
203.814 -48867
203.814 -48105
204.221 -48718
204.369 -47542
204.491 -46325
204.604 -46325
204.604 -46325
204.604 -46595
204.604 -47211
204.622 -47536
204.725 -47243
205.041 -47223
205.041 -45898
205.432 -46203
205.816 -46183
205.816 -44937
205.816 -44647
205.816 -44647
205.816 -43969
205.862 -43716
206.242 -44368
207.042 -43989
207.176 -42570
207.176 -41778
207.455 -41778
207.726 -41485
207.849 -42093
207.849 -42424
207.849 -42701
207.849 -43020
207.849 -43020
207.87 -43020
207.87 -43020
207.87 -43580
207.87 -42263
207.87 -41265
207.87 -40469
208.286 -40469
208.564 -40460
209.064 -40440
209.064 -40440
209.064 -40440
209.064 -41129
209.064 -39918
209.483 -39098
209.877 -39078
209.877 -39058
209.877 -39432
209.877 -39824
209.877 -38669
210.286 -39080
210.482 -38599
210.707 -38579
210.734 -38286
211.114 -38286
211.114 -38266
211.114 -38246
211.114 -37956
211.114 -37534
211.114 -36840
211.114 -37513
211.506 -36849
211.901 -37059
211.901 -37257
212.32 -37237
212.32 -37458
212.557 -37458
212.701 -37458
212.701 -38692
212.701 -38509
212.701 -38132
212.701 -38132
212.701 -38132
212.761 -38013
213.123 -38248
213.123 -37250
213.521 -37230
213.56 -37221
213.711 -36403
213.92 -37019
214.328 -37019
214.328 -37295
215.136 -37114
215.136 -36747
215.136 -35982
215.136 -36483
215.136 -36324
215.557 -35137
216.354 -35117
216.354 -35097
216.354 -33854
216.354 -33579
216.354 -33221
216.354 -32706
216.755 -32686
217.152 -32666
217.178 -35745
217.178 -38192
217.178 -41630
217.496 -41511
217.575 -39133
217.575 -39679
217.575 -39910
217.575 -40559
217.632 -40448
217.977 -40428
217.977 -40000
218.363 -39980
218.363 -39958
218.555 -39949
218.772 -38815
219.18 -37650
219.182 -38274
219.572 -38254
219.985 -38234
219.985 -38214
220.393 -37272
220.393 -36663
220.393 -37539
221.188 -37519
221.188 -36663
221.599 -36663
221.599 -36663
222.395 -36663
222.42 -36663
222.807 -36643
223.225 -36643
223.225 -35371
223.408 -34607
223.625 -34587
223.625 -35879
223.625 -34587
223.806 -34587
224.417 -34587
224.518 -34470
225.133 -33032
225.223 -33032
225.383 -32937
225.643 -32919
225.643 -32919
225.643 -31671
226.034 -31022
226.44 -30601
226.459 -30166
226.791 -30166
226.861 -30166
226.861 -31767
226.861 -33393
226.861 -33393
227.263 -34892
227.263 -36240
227.673 -37564
227.673 -39096
227.673 -40696
228.07 -42365
228.48 -43864
228.48 -43864
229.694 -43864
229.694 -43864
229.697 -43864
229.786 -43864
230.675 -43614
231.297 -43614
231.682 -43364
231.7 -45684
231.7 -48767
232.119 -48747
232.261 -46793
232.685 -46543
232.793 -46290
232.83 -45998
232.932 -46611
233.682 -46611
233.682 -46361
233.737 -46175
233.737 -45615
233.737 -44877
234.535 -42391
234.692 -42141
234.949 -40871
235.354 -41382
235.514 -41382
235.69 -41132
235.769 -41112
235.769 -41092
235.769 -40295
235.795 -40042
235.828 -39749
236.157 -39729
236.157 -39357
236.458 -39357
236.699 -39307
236.99 -39884
236.99 -39073
237.386 -39053
237.386 -39033
237.408 -38927
237.408 -37725
237.794 -37023
238.205 -36592
238.205 -37413
238.513 -37413
238.593 -37238
238.838 -36945
239.011 -36299
239.516 -35688
239.827 -34926
240.644 -34926
241.036 -34926
241.058 -34534
241.058 -33627
241.058 -32674
241.465 -31915
241.465 -31117
241.522 -31117
241.83 -30824
241.862 -30824
241.862 -30824
241.862 -31503
242.26 -31503
242.26 -30395
242.682 -30395
242.918 -30302
243.083 -30302
243.083 -29804
243.486 -29804
243.892 -29804
243.892 -29804
244.285 -29772
244.285 -29772
244.516 -29772
244.693 -29235
244.693 -30157
244.828 -30157
245.097 -29496
245.501 -29987
246.301 -29967
246.301 -29967
246.301 -29967
246.301 -29967
246.301 -28774
246.714 -28042
247.126 -28757
247.515 -28757
247.946 -28757
247.948 -28737
247.948 -28737
247.948 -28042
248.339 -28042
248.339 -28655
248.507 -28655
249.158 -28635
249.55 -29463
249.55 -28042
249.55 -28042
250.362 -27760
250.362 -27760
250.362 -27760
250.362 -28412
250.362 -27760
250.778 -27760
250.778 -27760
251.511 -27760
251.576 -27760
251.576 -28380
"""
    _, _, filenames = next(os.walk(tmpdir))

    assert len(filenames) == 1
    assert f"raid_damage.png" in filenames


def test_track_damage_character(script_runner, tmpdir):
    path = tmpdir.strpath
    ret = script_runner.run(python, "track_damage.py", log_file, character, "-e", "1", "-v", "--path", path)

    assert ret.success
    assert ret.stderr == ""

    assert ret.stdout == """\
162.518 -2009
174.245 -774
178.01 0
179.506 -1343
190.069 -1161
191.691 -873
192.494 -102
192.893 0
192.893 0
"""
    _, _, filenames = next(os.walk(tmpdir))

    assert len(filenames) == 1
    assert f"{character}_damage.png" in filenames
