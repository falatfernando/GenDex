import plotly.graph_objects as go
from django.shortcuts import render
from .forms import DNAInputForm

def home_view(request):
    """Render the home page with the DNA input form and results (if any)."""

    result_data = None
    plot_div = None

    if request.method == 'POST':
        form = DNAInputForm(request.POST)
        if form.is_valid():
            sequence = form.cleaned_data['sequence'].upper().replace('\n', '')

            # Basic stats:
            length = len(sequence)
            gc_count = sequence.count('G') + sequence.count('C')
            gc_content = (gc_count / length) * 100 if length > 0 else 0

            # Optional: base composition
            a_count = sequence.count('A')
            t_count = sequence.count('T')
            g_count = sequence.count('G')
            c_count = sequence.count('C')

            # Prepare result data
            result_data = {
                'length': length,
                'gc_content': round(gc_content, 2),
                'A': a_count,
                'T': t_count,
                'G': g_count,
                'C': c_count
            }

            # Create a simple Plotly pie chart of nucleotide composition
            fig = go.Figure(data=[go.Pie(labels=['A', 'T', 'G', 'C'],
                                         values=[a_count, t_count, g_count, c_count],
                                         hole=.4)])
            fig.update_layout(title_text="Nucleotide Composition")

            # Generate HTML div for the figure
            plot_div = fig.to_html(full_html=False)

    else:
        form = DNAInputForm()

    context = {
        'form': form,
        'result_data': result_data,
        'plot_div': plot_div,
    }
    return render(request, 'analysis/home.html', context)
