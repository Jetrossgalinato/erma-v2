/**
 * EmptyState Component
 *
 * Displays empty state when no facilities exist
 */

import React from "react";
import { Building } from "lucide-react";

const EmptyState: React.FC = () => {
  return (
    <div className="flex items-center justify-center min-h-[400px]">
      <div className="text-center">
        <Building className="h-16 w-16 text-gray-400 dark:text-gray-600 mx-auto mb-4" />
        <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">
          No Facilities Found
        </h3>
        <p className="text-gray-600 dark:text-gray-400">
          Get started by adding your first facility
        </p>
      </div>
    </div>
  );
};

export default EmptyState;
