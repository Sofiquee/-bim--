<html>
<head>
<title>Task3.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #bcbec4;}
.s1 { color: #bcbec4;}
.s2 { color: #6aab73;}
.s3 { color: #7a7e85;}
.s4 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Task3.py</font>
</center></td></tr></table>
<pre><span class="s0">list_players </span><span class="s1">= [</span><span class="s2">&quot;Маша&quot;</span><span class="s1">, </span><span class="s2">&quot;Петя&quot;</span><span class="s1">, </span><span class="s2">&quot;Саша&quot;</span><span class="s1">, </span><span class="s2">&quot;Оля&quot;</span><span class="s1">, </span><span class="s2">&quot;Кирилл&quot;</span><span class="s1">, </span><span class="s2">&quot;Коля&quot;</span><span class="s1">]</span>
<span class="s3"># индекс середины</span>
<span class="s0">middle_index </span><span class="s1">= </span><span class="s0">len</span><span class="s1">(</span><span class="s0">list_players</span><span class="s1">) // </span><span class="s4">2</span>
<span class="s0">first_team </span><span class="s1">= </span><span class="s0">list_players</span><span class="s1">[:</span><span class="s0">middle_index</span><span class="s1">]</span>
<span class="s0">second_team </span><span class="s1">= </span><span class="s0">list_players</span><span class="s1">[</span><span class="s0">middle_index</span><span class="s1">:]</span>

<span class="s0">print</span><span class="s1">(</span><span class="s0">first_team</span><span class="s1">)</span>
<span class="s0">print</span><span class="s1">(</span><span class="s0">second_team</span><span class="s1">)</span>
</pre>
</body>
</html>