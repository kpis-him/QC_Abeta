% Load and Clean Data
% Assuming Column 1 = Phi, Column 2 = Psi
wt_data = readmatrix('/Users/kushalpatil/Desktop/A_beta_proj/03_md/misc/rama_wildtype.csv', 'FileType', 'text', 'CommentStyle', {'#', '@'});
arc_data = readmatrix('/Users/kushalpatil/Desktop/A_beta_proj/md/misc/rama_arctic_1.csv', 'FileType', 'text', 'CommentStyle', {'#', '@'});

% Extract Phi (Column 1)
phi_wt = wt_data(:, 1);
phi_arc = arc_data(:, 1);

% Run the Test for Phi
[V_phi, p_phi] = kuiper_2sample(phi_wt, phi_arc);

fprintf('--- Results for Phi (Backbone) ---\n');
fprintf('Kuiper V-statistic: %.4f\n', V_phi);
fprintf('P-value: %.5f\n', p_phi);

function [V, p] = kuiper_2sample(data1, data2)
    % 1. Normalize both to [0, 1] range
    s1_raw = sort(mod(data1 + 180, 360) / 360);
    s2_raw = sort(mod(data2 + 180, 360) / 360);
    
    n1 = length(s1_raw);
    n2 = length(s2_raw);
    
    % 2. CRITICAL FIX: Handle duplicate angles from GROMACS
    [s1, ia1] = unique(s1_raw, 'last');
    f1_steps = ia1 / n1;
    
    [s2, ia2] = unique(s2_raw, 'last');
    f2_steps = ia2 / n2;
    
    % 3. Create combined unique axis for ECDF comparison
    all_points = unique([s1; s2]);
    
    % 4. Calculate Empirical CDFs using the unique sets
    f1 = interp1(s1, f1_steps, all_points, 'previous', 0);
    f2 = interp1(s2, f2_steps, all_points, 'previous', 0);
    
    % 5. Kuiper Statistic V = D+ + D-
    D_plus = max(f1 - f2);
    D_minus = max(f2 - f1);
    V = D_plus + D_minus;
    
    % 6. P-value Approximation
    neff = (n1 * n2) / (n1 + n2);
    lambda = V * (sqrt(neff) + 0.155 + 0.24/sqrt(neff));
    k = 1:100;
    p = sum(2 * (4*k.^2 * lambda^2 - 1) .* exp(-2 * k.^2 * lambda^2));
    p = max(0, min(1, p)); 
end