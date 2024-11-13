<html>
<head>
<title>Task1.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #bcbec4;}
.s1 { color: #bcbec4;}
.s2 { color: #2aacb8;}
.s3 { color: #cf8e6d;}
.s4 { color: #7a7e85;}
.s5 { color: #6aab73;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Task1.py</font>
</center></td></tr></table>
<pre><span class="s0">numbers </span><span class="s1">= [</span><span class="s2">2</span><span class="s1">, -</span><span class="s2">93</span><span class="s1">, -</span><span class="s2">2</span><span class="s1">, </span><span class="s2">8</span><span class="s1">, </span><span class="s3">None</span><span class="s1">, -</span><span class="s2">44</span><span class="s1">, -</span><span class="s2">1</span><span class="s1">, -</span><span class="s2">85</span><span class="s1">, -</span><span class="s2">14</span><span class="s1">, </span><span class="s2">90</span><span class="s1">, -</span><span class="s2">22</span><span class="s1">, -</span><span class="s2">90</span><span class="s1">, -</span><span class="s2">100</span><span class="s1">, -</span><span class="s2">8</span><span class="s1">, </span><span class="s2">38</span><span class="s1">, -</span><span class="s2">92</span><span class="s1">, -</span><span class="s2">45</span><span class="s1">, </span><span class="s2">67</span><span class="s1">, </span><span class="s2">53</span><span class="s1">, </span><span class="s2">25</span><span class="s1">]</span>
<span class="s4"># TODO заменить значение пропущенного элемента средним арифметическим</span>
<span class="s0">sum </span><span class="s1">= </span><span class="s0">sum</span><span class="s1">(</span><span class="s0">num </span><span class="s3">for </span><span class="s0">num </span><span class="s3">in </span><span class="s0">numbers </span><span class="s3">if </span><span class="s0">num </span><span class="s3">is not None</span><span class="s1">)</span>
<span class="s0">ccount </span><span class="s1">= </span><span class="s0">len </span><span class="s1">(</span><span class="s0">numbers</span><span class="s1">)</span>
<span class="s0">average_of_numbers </span><span class="s1">= </span><span class="s0">sum</span><span class="s1">/</span><span class="s0">ccount</span>
<span class="s0">numbers</span><span class="s1">[</span><span class="s2">4</span><span class="s1">]= </span><span class="s0">average_of_numbers</span>
<span class="s0">print</span><span class="s1">(</span><span class="s5">&quot;Измененный список:&quot;</span><span class="s1">, </span><span class="s0">numbers</span><span class="s1">)</span>
</pre>
</body>
</html>