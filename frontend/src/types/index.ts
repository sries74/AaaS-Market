export interface User {
  id: string;
  email: string;
  credits: number;
  createdAt: string;
}

export interface Agent {
  id: string;
  name: string;
  description: string;
  category: string;
  creditCost: number;
  isActive: boolean;
}

export interface AgentRun {
  id: string;
  agentId: string;
  userId: string;
  status: "pending" | "running" | "completed" | "failed";
  input: Record<string, unknown>;
  output: Record<string, unknown> | null;
  createdAt: string;
  completedAt: string | null;
}

export interface ApiResponse<T> {
  success: boolean;
  data: T | null;
  error: string | null;
  meta?: {
    total: number;
    page: number;
    limit: number;
  };
}
