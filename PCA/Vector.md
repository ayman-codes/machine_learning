<center><h2 style='background:purple; font-family:cursive; border-radius:20px; width:200px;'>Vector space</h2></center>

<b>Proof of Vector space</b>
<blockquote>
<b>Addition properties</b>

<ol type='I'>
<li><b>Closure under Addition:</b> u+v ∈ V</li>
<li><b>Commutativity of addition:</b> u+v = v+u</li>
<li><b>Associativity of addition:</b> u+(v + w) = w + (u + v)</li>
<li><b>Existence of an additive identity:</b> 0 ∈ V where 0 + u = u</li>
<li><b>Existence of additive inverses:</b> For every vector u in V, there exists a vector -u in V such that u + (-u) = 0.</li>
</ol>

<b>scalar multiplication properties</b>
<ol type='I'>
<li><b>Closure under scalar multiplication:</b> cu ∈ V</li>
<li><b>Associativity of scalar multiplication:</b> c(u + v) = cu + cv</li>
<li><b>Distributivity of scalar multiplication  with respect to scalar addition:</b> (c + d)u = cu + du</li>
<li><b>Distributivity of scalar multiplication with respect to vector addition:</b>  c(du) = (cd) u</li>
<li><b>Identity element of scalar multiplication:</b> 1u = u</li>
</ol>
</blockquote>



<h3 style='background:crimson; font-family:cursive; border-radius:10px; width:280px;'>Prove that R^2 is a vector space</h3>
<blockquote>
<ol>
<li>Closure under Addition: for any vectors in R^2 their addition should be in R^2 because the sum of any real numbers and then the square of them is a positive real number</li>

<li>Commutativity of addition: for any v=(x1,y1) and u=(x2,y2) the addition of v+u = u+v where
{(x1+x2), (y1+y2)} = {(x2+x1), (y2+y1)} </li>

<li>Associativity of addition: u=(x1, y1) v=(x2, y2) w=(x3, y3) where w + (u + v) = u + (w + v)
(x3, y3) + {(x1, y1), (x2, y2)} = (x1, y1) + {(x3, y3), (x2, y2)} where w,u,v belongs to R^2</li>

<li>Existence of an additive identity: There exists a vector (0, 0) in R^2 such that for any vector (a, b) in R^2, (0, 0) + (a, b) = (a + 0, b + 0) = (a, b). Therefore, (0, 0) serves as the additive identity.</li>

<li>Existence of additive inverses: for u = (x1, y1) where u belongs to R^2 (x1, y1) + -(x1, y1)
= (0, 0). since the square of any positive or negative number is positive</li>

<li>Closure under scalar multiplication: for u = (x1, y1) and and scalar c c*u belongs to V, for example u = (1, 2) c=2 c*u = (2, 4) which belongs to R^2</li>

<li>Associativity of scalar multiplication: For any scalar c and d and vector (a, b) in R^2, (cd)(a, b) = c(d(a, b)) = c(da, db) = (cda, cdb).</li>

<li>Distributivity of scalar multiplication  with respect to scalar addition: For any scalars c and d and vectors (a, b) and (e, f) in R^2, c((a, b) + (e, f)) = c(a + e, b + f) = (c(a + e), c(b + f)) = (ca + ce, cb + cf) = (ca, cb) + (ce, cf) = c(a, b) + c(e, f).</li>

<li>Distributivity of scalar multiplication with respect to vector addition: For any scalars c and d and vector (a, b) in R^2, (c + d)(a, b) = ((c + d)a, (c + d)b) = (ca + da, cb + db) = (ca, cb) + (da, db) = c(a, b) + d(a, b).</li>

<li>Identity element of scalar multiplication: For any vector (a, b) in R^2, 1(a, b) = (1a, 1b) = (a, b). Therefore, 1 serves as the scalar identity.</li>

</ol>
</blockquote>



<h3 style='background:crimson; font-family:cursive; border-radius:10px; width:470px;'>Prove that V = {[X Y], x >= 0 and y >= 0} is not vector space</h3>
<blockquote>
<ol>
<li> <b>Closure under Addition:</b> for any x and y that are positive their addition must also be positive since the sum of any 2 positive numbers is positive so it satisfies </li>
<li> <b>Closure under scalar multiplication:</b> cu ∈ V, where u = (x1, y1) and c is a negative number for example c = -1, hence c*u = (-x1, -y1) which is not ∈ V</li>
</ol>
</blockquote>



<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:400px;'>Prove that V = {[X Y], xy >= 0} is not vector space</h3>
<blockquote>

<b>Closure under Addition:</b> u = [1, 2] and v = [-2, -1] where both u and v are ∈ V u + v = [ 1 + (-2), 2 + (-1)] = [-1, 1] since -1 * 1 = -1 and -1 is not greater than or equals zero we can say that V is not a vector space
</blockquote>


---

<center><h2 style='background:purple; font-family:cursive; border-radius:20px; width:200px;'>Subspaces</h2></center>

<b>Conditions</b>
<blockquote>
<ol type='1'>
<li>V != 0</li>
<li>x, y ∈ V then x + y ∈ V</li>
<li> c ∈ V, x ∈ V = xc ∈ V</li>
</ol>
</blockquote>

<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:560px;'>Prove that V = { [x1 x2, x3] ∈ R^3 | x3 = x1+x2} is a subspace of R^3</h3>
<blockquote>
<ol>
<li>0 = 0 + 0, where [0, 0, 0] ∈ V, so V != 0</li>
<li> for X = [x1, x2, x3], Y = [y1, y2, y3] where X,Y ∈ V. and X3 = X1 + X2 and Y3 = Y1 + Y2
so, X + Y = [(x1+y1), (x2+y2), (x3+y3)] where x3 + y3 = (x1 + x2) + (y1 + y2) so X3 + Y3 = (x1 + y1) + (x2 + y2)</li>
<li>for c ∈ V and X = [x1, x2, x3] ∈ V where x3 = x1 + x2, xc ∈ V. So, c*x3 = c(x1 + x2) => c*x3 = cx1 + cx2, so cX ∈ V</li>
</ol>
</blockquote>

<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:560px;'>Prove that Let S={(x1 ,x2) |x2 = 2x1}. Prove that S is a subspace of R^2</h3>
<blockquote>
<ol>
<li> [0, 0] ∈ S, where x2 = 2x1 so, X2 = 2 * 0 = 0 => X2 = 0 so therefor the zero vector is in S in other words S != 0</li>
<li> for u = (x1, x2) and v = (y1, y2) where x2 = 2x1 and y2 = 2y1. so, u + v = {(x1 + y1), (x2 + y2)} => (x1 + y1), (2x1 + 2y1) => u + v = {(x1 + y1), 2(x1 + y1)}</li>
<li> for c ∈ V and u = (x1, x2) where x2 = 2x1 so cx2 = c*2x1</li>
</ol>
</blockquote>

<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:460px;'>Prove that S={(x1,x2,x3)’ | x1 = x2} is a subspace of R^3</h3>
<blockquote>
<ol>
<li>To prove that S is not empty and contains the zero vector, assume that v = (x1, x2, x3) where x1 = x2, so, v = [0, 0, 0] where x1 = x2 => x1 = 0 </li>
<li>assume that v = (x1, x2, x3) and u = (y1, y2, y3) u + v = {(x1+y1) + (x2+y2) + (x3+y3)} where x1 = x2 and y1 = y2 we get u + v = {(x1+y1) (x1+y1) (x3+y3)} ∈ S</li>
<li>Assume that we have a constant c and v = (x1, x2, x3) where x1=x2, so c*v = c(x1, x2, x3) where x1 = x2 => c*v = c(x1, x1, x3) => c*v = cx1, cx1, cx2</li>
</ol>
</blockquote>


<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:510px;'>Prove that S = {(x1, 1)’  | x real number} is <b>NOT</b> a subspace of R^2</h3>
<blockquote>
<ol>
<li> <b>Zero Vector: </b> The zero vector of R^2 is (0, 0), However zero vector is not in S because, we have a constant which is 1 so (0, 0) != (0, 1) PROVES THAT S IS NOT A SUBSPACE OF R^2</li>
</ol>
</blockquote>

<center><h2 style='background:purple; font-family:cursive; border-radius:20px; width:300px;'>Span and Spanning Sets</h2></center>
<ol>
<li><b>Linear combination: </b> is the combination of vectors and constants, (aI', bJ')</li>
<li><b>Span: </b> is the set of all linear combination of I' and J' or V and W</li>
<li> <b>Linearly Independent: </b>if a vector adds another dimension to the span.
linearly independent if c1∙v1 + c2∙v2 + … + cn∙vn = 0 if ci=0 for all i = 1,…,n</li>
<li>The vectors {v1, v2, …, vn} form a <b>basis</b> for the vector space V if and only if:
<ul>
<li>v1 ,v2 , …, vn are linearly independent</li>
<li>V=span(v1, v2, …, vn)</li></ul>
</li>
</ol>

<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:810px;'>Prove that the following vectors are NOT linearly independent: v1=(1,-1,2)’, v2=(-2,3,1)’, v3=(-1,3,8)’
</h3>
<blockquote>
<ol>
<li>So we have to prove that it is linearly dependent, and to do that we should find c1, c2 and c3 values that are not equal to zero</li>
<li>We can use the matrix form to solve</li>

1   -1   2    |   0
              
-2   3   1    |   0

-1   3   8    |   0

<li>Using low echelon form we get </li>

1   0   7   |   0

0   1   5   |   0

0   0   0   |   0
<li>So we get equation 1) c1 + 7c3 = 0</li>
<li>So we get equation 2) c2 + 5c3 = 0</li>
<li>C3 is a free variable so let's substitute with 1</li>
<li>C1 = -7(1) & c2 = -5(1)</li>
<li>We get c1 = -7, c2 = -5 and c3 = 1</li>
<li>So there exist non zero vector thus proving that this vector is linearly dependent</li>
</ol>
</blockquote>

<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:810px;'>Prove that e1=(1,0)’, e2=(0,1)’ is a basis for R^2
</h3>
<blockquote>
<ol>
<b>First we have to prove it can be expressed as a linear combination so that they are span of R^2</b>
<li> let's take vector (x,y) in R^2 such that c1e1 + c2e2 = (x, y).

v = c1 * (1, 0) + c2 * (0, 1) => (c1, 0) + (0, c2) = (x, y).

Simplifying we get (c1, c2) = (x, y).

We can substitute the scalars with any real numbers as well and we arrive to the conclusion that c1=x and c2=y Therefore, any vector (x, y) in R^2 can be expressed as a linear combination of e1 and e2.
</li>

<b>Proving Linearly independence by finding trivial solution, where c1 = 0 and c2 = 0.</b>
<li>c1(1,0) + c2(0,1) = (0,0)

(c1, 0) + (c2,1) =(0, 0)

so c1=0 and c2=0, so it is linearly independent proving that it is the basis for R^2
</li>
</ol>
</blockquote>

<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:810px;'>Prove that {(1,1,1)’, (0,1,1)’,(2,0,1)} and {(1,1,1)’, (1,1,0)’,(1,0,1)’} are both basis for R^3
</h3>
<blockquote>
<b>First let's take {(1,1,1)’, (0,1,1)’,(2,0,1)} as v1 and {(1,1,1)’, (1,1,0)’,(1,0,1)’} as v2</b>

<b>Solving for v1</b>
<ol>
<li><b>Proof of span: </b> c1(1,1,1) + c2(0,1,1) + c3(2,0,1) = (x, y, z)

c1 + 2c3 = x

c1 + c2 = y

c1 + c2 + c3 = z

we can solve for c1 in the first equation c1 = x - 2c3

<b> substituting c1 in the second equation we get</b>

x - 2c3 + c2 = y => c2 = y - x + 2c3

<b>Substituting c2 in the third equation we get</b>

(x - 2c3) + (y - x + 2c3) + c3 = z

y - c3 = z => c3 =  z - y

<b>The new system of equations is: </b>

c1 = x - 2c3

c2 = y - x + 2c3

c3 = z - y

c1(1,1,1) + c2(0,1,1) + c3(2,0,1) = (x, y, z)

(x - 2c3, x - 2c3, x - 2c3) + (y - x + 2c3, y - x + 2c3) + (2z - 2y, z - y) = v

(x - 2c3) + (2z - 2y, z - y) = v

(x - (2z - 2y)) + (2z - 2y, z - y) = v

<b>Substitute c3 with y-z</b>

v = (x, y, z)
</li>

<li> <b>Linear independency: </b> c1(1,1,1) + c2(0,1,1) + c3(2,0,1) = (0, 0, 0)

c1 + 2c3 = 0

c1 + c2 = 0

c1 + c2 + c3 = 0

c1 = -2c2

c3 = c2

c1 = -c2

-2c2 + c2 + -c2 = 0

so we get -2c2 = 0

so c1 = 0

0 + 2c3 = 0 => c3 = 0/2 => c3 = 0

0 + c2 + 0 = 0 => c2 = 0

so we find that c1=c2=c3 = 0 means that the vectors are linearly independent.
</li>


<b> Now that we have proven the span and linear independence we can conclude that v1 is a basis of R^3</b>
</ol>


---

<b>let v2 = {(1,1,1)’, (1,1,0)’,(1,0,1)’} solving for v2</b>


<ol>
<li><b>Span: </b> c1(1, 1, 1) + c2(1, 1, 0) + c3(1, 0, 1) = (x, y, z)

c1 + c2 + c3 = x

c1 + c2 = y

c1 + c3 = z

================================================================================

c1 + c2 + c3 = x

c1 = y - c2

c3 = z - c1

================================================================================

c1 = y - c2

c2 = x - c1 - c3

c3 = z - c1

================================================================================

y-c2(1, 1, 1) + (x - c1 - c3)(1, 1, 0) + (z - c1)(1, 0, 1) = v

v = (x, y, z)
</li>

<li><b>Linearly independence: </b>

c1 + c2 + c3 = 0

c1 + c2 = 0

c1 + c3 = 0

================================================================================

c1 = -c2 - c3

-c2 - c3 + c2 = 0 => c3 = 0

c1 + c3 = 0 ==> c1 + 0 = 0 ==> c1 = 0

================================================================================

0 + c2 + 0 = 0

c2 = 0

<b>so we get c1=c2=c3=0 thus proving linear independency</b>

</li>
</ol>

<b>So both v1 and v2 are bases of R^3</b>

</blockquote>

<center><h2 style='background:lime; color:black; font-family:cursive; border-radius:20px; width:300px;'>Span and Spanning Sets</h2></center>

<h3 style='background:crimson; font-family:cursive;border-radius:10px; width:810px;'>Prove that {(1,1,1)’, (0,1,1)’,(2,0,1)} and {(1,1,1)’, (1,1,0)’,(1,0,1)’} are both basis for R^3
</h3>