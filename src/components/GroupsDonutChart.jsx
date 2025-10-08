/**
 * Serves as a donut chart to show the distribution of groups and teams.
 */


import React from 'react';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

// Register Chart.js components
ChartJS.register(
  ArcElement,
  Tooltip,
  Legend
);

function GroupsDonutChart({ data }) {
  const totalGroups = data.length;
  const totalTeams = data.reduce((sum, group) => sum + group.teamCount, 0);

  const chartData = {
    labels: ['Total Groups', 'Total Teams'],
    datasets: [
      {
        data: [totalGroups, totalTeams],
        backgroundColor: [
          'rgba(59, 130, 246, 0.8)',   // Blue for groups
          'rgba(16, 185, 129, 0.8)',   // Green for teams
        ],
        borderColor: [
          'rgba(59, 130, 246, 1)',
          'rgba(16, 185, 129, 1)',
        ],
        borderWidth: 2,
        cutout: '60%',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          font: {
            family: '-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, sans-serif',
            size: 12,
            weight: '500',
          },
          color: '#64748b',
          padding: 20,
          usePointStyle: true,
          pointStyle: 'circle',
        },
      },
      tooltip: {
        backgroundColor: 'rgba(255, 255, 255, 0.95)',
        titleColor: '#1e293b',
        bodyColor: '#475569',
        borderColor: '#e2e8f0',
        borderWidth: 1,
        cornerRadius: 12,
        displayColors: false,
        titleFont: {
          family: '-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, sans-serif',
          size: 14,
          weight: 'bold',
        },
        bodyFont: {
          family: '-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, sans-serif',
          size: 13,
        },
        padding: 12,
        callbacks: {
          title: function(context) {
            return context[0].label;
          },
          label: function(context) {
            const value = context.parsed;
            const total = context.dataset.data.reduce((a, b) => a + b, 0);
            const percentage = ((value / total) * 100).toFixed(1);
            return `${value} (${percentage}%)`;
          },
        },
      },
    },
    animation: {
      duration: 1000,
      easing: 'easeInOutQuart',
    },
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4 hover:shadow-md transition-shadow">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-lg font-semibold text-gray-900 mb-1">Organization Overview</h3>
          <p className="text-sm text-gray-600">Groups vs Teams distribution</p>
        </div>
        <div className="flex items-center space-x-2 text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded-full">
          <div className="w-2 h-2 bg-violet-400 rounded-full animate-pulse"></div>
          <span>Live</span>
        </div>
      </div>
      
      <div className="h-64 w-full relative">
        <Doughnut data={chartData} options={options} />
        
        {/* Center text */}
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="text-center">
            <div className="text-2xl font-bold text-gray-900">{totalGroups}</div>
            <div className="text-xs text-gray-600 font-medium">Groups</div>
          </div>
        </div>
      </div>
      
      <div className="mt-3 pt-3 border-t border-gray-200">
        <div className="grid grid-cols-2 gap-4 text-sm">
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-indigo-500 rounded-full"></div>
            <span className="text-gray-600">Groups</span>
            <span className="font-semibold text-gray-900">{totalGroups}</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-violet-500 rounded-full"></div>
            <span className="text-gray-600">Teams</span>
            <span className="font-semibold text-gray-900">{totalTeams}</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default GroupsDonutChart;
