# Extrapolation Experimentalist

The extrapolation sampling method identifies novel experimental conditions where the prediction of a
model exhibits the highest slope compared to already existing data.

For each novel condition, denoted as $x_i$, with its corresponding prediction $y_{\text{pred}, i}$,
the process begins by identifying the nearest existing datapoint, $x_{\text{nearest}, i}$, which has
an associated observed value $y_{\text{existing}, i}$. The slope between these points is then
calculated as follows:

$$ m_i = \frac{y_{\text{pred}, i}-y_{\text{existing}, i}}{x_i-x_{\text{nearest}, i}} $$

The condition with the highest slope is selected first:

$$ \underset{i}{argmax}(m_i) $$

