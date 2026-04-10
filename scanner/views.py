from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import ScanReport
from .recon_engine import ReconScanner

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    # History of scans
    scans = ScanReport.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'scanner/dashboard.html', {'scans': scans})

@login_required
def new_scan(request):
    if request.method == 'POST':
        target = request.POST.get('target')
        selected_modules = request.POST.getlist('scan_modules')
        
        scanner = ReconScanner(target)
        
        # 1. Initialize all to None (Skipped)
        ports_data = None
        headers_data = None
        dirs_data = None

        # 2. Only run scans if the flag is in selected_modules
        
        # [P] Port Scan Logic
        if 'ports' in selected_modules:
            do_service_detect = 'services' in selected_modules
            ports_data = scanner.run_port_scan(detect_services=do_service_detect)
            # If scan returns nothing, ensure it's an empty list [], not None
            if ports_data is None: ports_data = [] 

        # [H] Headers Logic
        if 'headers' in selected_modules:
            headers_data = scanner.check_headers()

        # [D] Directory Logic
        if 'dirs' in selected_modules:
            dirs_data = scanner.dir_bruteforce()
            if dirs_data is None: dirs_data = []

        # 3. Save to Database
        report = ScanReport.objects.create(
            user=request.user,
            target=target,
            open_ports=ports_data,       # Will be None if skipped, [] if empty, or Data
            headers_info=headers_data,   # Will be None if skipped
            found_directories=dirs_data  # Will be None if skipped
        )
        return redirect('scan_detail', pk=report.pk)
        
    return render(request, 'scanner/new_scan.html')

@login_required
def scan_detail(request, pk):
    report = get_object_or_404(ScanReport, pk=pk, user=request.user)
    return render(request, 'scanner/scan_detail.html', {'report': report})