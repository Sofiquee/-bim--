<html>
<head>
<title>Task2.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #bcbec4;}
.s1 { color: #bcbec4;}
.s2 { color: #2aacb8;}
.s3 { color: #6aab73;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Task2.py</font>
</center></td></tr></table>
<pre>
<span class="s0">vol </span><span class="s1">= </span><span class="s2">1.44 </span><span class="s1">* </span><span class="s2">1024 </span><span class="s1">* </span><span class="s2">1024</span>
<span class="s0">pages </span><span class="s1">= </span><span class="s2">100</span>
<span class="s0">lines_per_page </span><span class="s1">= </span><span class="s2">50</span>
<span class="s0">chars_in_line </span><span class="s1">= </span><span class="s2">25</span>
<span class="s0">volume_for_char </span><span class="s1">= </span><span class="s2">4</span>
<span class="s0">print</span><span class="s1">(</span><span class="s3">&quot;Количество книг, помещающихся на дискету:&quot;</span><span class="s1">, </span><span class="s0">int</span><span class="s1">(</span><span class="s0">vol </span><span class="s1">// (</span><span class="s0">pages</span><span class="s1">*</span><span class="s0">lines_per_page</span><span class="s1">*</span><span class="s0">chars_in_line</span><span class="s1">*</span><span class="s0">volume_for_char</span><span class="s1">) ))</span></pre>
</body>
</html>